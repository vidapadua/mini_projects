# Stock News SMS Alert

This project uses the [Alpha Vantage API](https://www.alphavantage.co/documentation/#daily) for stock data and [News API](https://newsapi.org/docs) for fetching relevant news articles. When the stock price of Costco (COST) increases or decreases by 5% between yesterday and the day before, the program retrieves news articles covering potential reasons for the change. If a significant change occurs, an SMS notification is sent using Twilio.

---

#### API Documentation:
- [Alpha Vantage API](https://www.alphavantage.co/documentation/#daily)
- [News API](https://newsapi.org/docs) 
- [Twilio API SMS Messaging](https://www.twilio.com/docs/libraries/reference/twilio-python/)

#### API Endpoint:
- [STOCK_ENDPOINT](https://www.alphavantage.co/query)
- [NEWS_ENDPOINT](https://newsapi.org/v2/everything)

#### Improvements:
With more time a GUI can be used to build this project further, a simple 
tkinter would suffice although more advanced ones can be used.
Instead of using a predetermined Stock, in this case COSTCO, it can instead ask for input
from the user what Stock they would like to track, frequency of notice, % difference and more 
news source. 
Additionally instead of just one stock, this can easily
handle multiple stocks like an investment portfolio. 
Another improvement is to add this to Pythoneverywhere so it can automatically
send SMS on a daily, or even more often basis. 

## Modules/Libraries


- `requests` – Fetches data from the APIs.
- `pytz` – Handles timezone conversions.
- `datetime` – Manages date operations.
- `newsapi` – Fetches relevant news articles.
- `twilio.rest` – Sends SMS notifications.