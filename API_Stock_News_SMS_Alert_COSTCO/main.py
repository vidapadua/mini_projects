from api_key import *
import requests
from datetime import datetime, timedelta, UTC
import pytz
from newsapi import NewsApiClient
from twilio.rest import Client




STOCK_NAME = "COST"
COMPANY_NAME = "Costco"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"




def run_main():
    yesterday_str, day_before_str= get_dates()
    close_price_yesterday = None
    close_price_day_before = None
    send_sms_check = False

    stock_param= {
        'function':'TIME_SERIES_DAILY',
        'symbol':STOCK_NAME,
        'apikey':get_api_key_stocks()
    }

    stock_url = 'https://www.alphavantage.co/query'
    r = requests.get(url=stock_url,params=stock_param)
    data = r.json()

    print(f"\nNews will be printed out and sent to SMS if the change in value of stock {STOCK_NAME} {COMPANY_NAME} is greater than 5%.")


    for date in data['Time Series (Daily)']:
        if date == yesterday_str:
            close_price_yesterday = data['Time Series (Daily)'][date]['4. close']
        elif date == day_before_str:
            close_price_day_before = data['Time Series (Daily)'][date]['4. close']
        else:
            break

    difference =(float(close_price_yesterday)-float(close_price_day_before))/float(close_price_day_before)
    difference = round(difference,4) *100


    if abs(float(difference))>5:
        get_news(difference)

    else:
        print(f"Change is Not Significant. Percent change is {round(difference,2)}%")
        print("No SMS will be sent.")




def get_dates():
    eastern_tz = pytz.timezone('US/Eastern')
    eastern_time = datetime.now(eastern_tz)
    weekday = eastern_time.weekday()

    if weekday == 5:
        yesterday = eastern_time - timedelta(days=1)
        day_before = eastern_time - timedelta(days=2)
        print(f"Data was retrieved from {day_before.strftime('%Y-%m-%d')} and {yesterday.strftime('%Y-%m-%d')} due to the stock market being closed today.")
    elif weekday == 6:
        yesterday = eastern_time - timedelta(days=2)
        day_before = eastern_time - timedelta(days=3)
        print(f"Data was retrieved from {day_before.strftime('%Y-%m-%d')} and {yesterday.strftime('%Y-%m-%d')} due to the stock market being closed today.")
    else:
        yesterday = eastern_time - timedelta(days=1)
        if yesterday.weekday() == 6:
            yesterday -= timedelta(days=2)
            day_before = yesterday - timedelta(days=1)
        elif yesterday.weekday() == 5:
            yesterday -= timedelta(days=1)
            day_before = yesterday - timedelta(days=1)
        else:
            day_before = yesterday - timedelta(days=1)

        print(f"Data was retrieved from {day_before.strftime('%Y-%m-%d')} and {yesterday.strftime('%Y-%m-%d')}.")


    yesterday_str = yesterday.strftime('%Y-%m-%d')
    day_before_str = day_before.strftime('%Y-%m-%d')

    return yesterday_str, day_before_str



def get_news(difference):
    newsapi = NewsApiClient(api_key=get_api_key_news())

    today = datetime.now(UTC)  # Corrected: Use timezone-aware UTC time
    three_days_ago = today - timedelta(days=3)

    news_data = newsapi.get_everything(
        q=COMPANY_NAME,
        language="en",
        sources="cnbc, bloomberg, forbes, business-insider",
        from_param=three_days_ago.strftime("%Y-%m-%d"),
        to=today.strftime("%Y-%m-%d"),
        sort_by="publishedAt",
        page_size=3
    )
    print("RECENT HEADLINES:")
    # print(f"Total Number of Articles: {len(news_data['articles'])} Articles\n")

    # Check if there are articles
    if news_data.get("articles"):
        for article in news_data["articles"]:
            message=""
            if difference>0: message+=f"🔺{round(difference,2)}%"
            elif difference==0: pass
            else: message+=f"🔻{round(difference,2)}%"

            full_message = (
                f"{STOCK_NAME}: {message}\n"
                f"Headline: {article['title']}\n"
                f"Brief: {article['description']}\n"
                f"Source: {article['source']['name']}\n"
                f"URL: {article['url']}\n"
            )

            send_sms(full_message)

    else:
        print("No news articles found.")



def send_sms(full_message):

    print("Headlines will be sent to SMS.")
    client = Client(get_user_account_sid(), get_user_auth_token())
    message = client.messages.create(
        body=full_message,
        from_=get_user_from_number(),
        to=get_user_verified_calling_number()
    )

    print(f"SMS sent: {full_message}")



run_main()
