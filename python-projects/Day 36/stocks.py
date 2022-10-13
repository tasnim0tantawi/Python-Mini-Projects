import requests
import datetime

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc."
END_POINT_STOCK = "https://www.alphavantage.co/query"
STOCK_KEY = " Z3C2XIDMYF5PQFDY"
END_POINT_NEWS = "https://newsapi.org/v2/everything"
NEWS_KEY = "7496029ad5864a6fb43d8dcab16c2574"
stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_KEY
}
response = requests.get(END_POINT_STOCK, params=stock_parameters)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
closing_price = data_list[0]["4. close"]
prev_closing_price = data_list[1]["4. close"]
change = round(abs(float(closing_price) - float(prev_closing_price)), 2)
change_percent = round((change / float(prev_closing_price)) * 100, 2)
if change_percent > 5:
    news_parameters = {
        "qInTitle": COMPANY_NAME,
        "apiKey": NEWS_KEY
    }
    news_response = requests.get(END_POINT_NEWS, params=news_parameters)
    news_data = news_response.json()["articles"]
    three_news = news_data[:3]
    formatted_news = [f"Title: {article['title']}\nBrief: {article['description']}" for article in three_news]
    print(formatted_news[0])


