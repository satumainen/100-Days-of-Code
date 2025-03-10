STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_TYPE = "TIME_SERIES_DAILY"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

import os
import requests
from twilio.rest import Client

#fetch environmental variables
STOCK_API_KEY = os.environ.get('STOCK_API_KEY')
NEWS_API_KEY = os.environ.get('NEWS_API_KEY')

stock_params = {
    "function": API_TYPE,
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

"""
Get the difference in stock prices in two days for the chosen company.
"""

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"] #go to the time series dictionary, dates are keys

data_list = [value for (key, value) in data.items()] #list comprehension

#yesterday's closing price
yesterday_data = data_list[0]
yesterday_closing_price = float(yesterday_data["4. close"])

#prices day before yesterday
dbf_yesterday_data = data_list[1]
dbf_yesterday_closing_price = float(dbf_yesterday_data["4. close"])

#difference
pos_difference = yesterday_closing_price - dbf_yesterday_closing_price
up_down = None
if pos_difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

#percentage difference in price between closing price yesterday and closing price the day before yesterday
perc_difference = round((pos_difference / yesterday_closing_price) * 100)

"""
If the difference in stock prices is over 5%, send three news articles to the specified phone number. 
"""

if abs(perc_difference) > 5:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }

    #get the three newest news
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    three_articles = news_response.json()["articles"][:3]

    #new list of the first 3 article headline and description using list comprehension.
    formatted_articles_list = [f"{STOCK_NAME}: {up_down} {perc_difference}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]

    #Send Twilio SMS, fetch environmental variables
    account_sid = os.environ.get('ACC_SID')
    auth_token = os.environ.get("AUTH_TOKEN")
    my_twilio_nr = os.environ.get("MY_TWILIO_NR")
    my_phone_number = os.environ.get("MY_NR")

    client = Client(account_sid, auth_token)

    for article in formatted_articles_list:
        message = client.messages.create(
            body=article, #each formatted_articles_list item
            from_=my_twilio_nr,
            to=my_phone_number,
        )


