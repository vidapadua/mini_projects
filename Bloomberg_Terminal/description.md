# Bloomberg

This project uses the [Alpha Vantage API](https://www.alphavantage.co/documentation/#daily) 
for stock end point and [News API](https://newsapi.org/docs) for the news end point. 
Together when stock price increase/decreases by 5% between yesterday and the day 
before yesterday and find relevant news covering why.  


#### API Documentation:
- [Alpha Vantage API](https://www.alphavantage.co/documentation/#daily)
- [News API](https://newsapi.org/docs) 

#### API Endpoint:
- [STOCK_ENDPOINT](https://www.alphavantage.co/query)
- [NEWS_ENDPOINT](https://newsapi.org/v2/everything)

## Modules/Libraries

- `requests`: Used for making HTTP requests to fetch data from the API.
- `tkinter`: Used for creating the graphical user interface (GUI). It provides windows, buttons, labels, and other UI elements for user interaction.
