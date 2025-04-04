from api_key import *
import requests
from datetime import datetime, timedelta, UTC
import pytz
from newsapi import NewsApiClient



# STOCK_NAME = "COST"
# COMPANY_NAME = "Costco Wholesale Corp"
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla"
# COMPANY_NAME = "Donald Trump"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").




def get_stocks_data():
    yesterday_str, day_before_str= get_dates()
    close_price_yesterday = None
    close_price_day_before = None

    stock_param= {
        'function':'TIME_SERIES_DAILY',
        'symbol':STOCK_NAME,
        'apikey':get_api_key_stocks()
    }

    stock_url = 'https://www.alphavantage.co/query'
    r = requests.get(url=stock_url,params=stock_param)
    data = r.json()

    for date in data['Time Series (Daily)']:
        if date == yesterday_str:
            print(data['Time Series (Daily)'][date])
            close_price_yesterday = data['Time Series (Daily)'][date]['4. close']
        elif date == day_before_str:
            print(data['Time Series (Daily)'][date])
            close_price_day_before = data['Time Series (Daily)'][date]['4. close']
        else:
            break

    difference =(float(close_price_yesterday)-float(close_price_day_before))/float(close_price_day_before)
    difference = round(difference,4) *100

    if abs(float(difference))>5:
        print(f"Get News its over 5% - {round(difference,2)}\n")
    else:
        print(f"Not Significant {round(difference,2)}\n")

    get_news(difference)




def get_dates():
    eastern_tz = pytz.timezone('US/Eastern')
    eastern_time = datetime.now(eastern_tz)
    yesterday=eastern_time- timedelta(days=1)
    day_before=yesterday- timedelta(days=1)
    yesterday_str = yesterday.strftime('%Y-%m-%d')
    day_before_str = day_before.strftime('%Y-%m-%d')
    return yesterday_str,day_before_str

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

            print(f"{STOCK_NAME}:{message}")
            print(f"Headline: {article['title']}")
            print(f"Brief: {article['description']}")
            print(f"Source: {article['source']['name']}")
            print(f"URL: {article['url']}\n")
    else:
        print("No news articles found.")


get_stocks_data()


#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

#TODO 2. - Get the day before yesterday's closing stock price

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

