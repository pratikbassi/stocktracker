import requests
import os
import datetime
from dotenv import load_dotenv


#make an api call to alphavantage and get the data
def get_data(ticker):
  load_dotenv()
  API_KEY = os.getenv('API_KEY')
  intraday = requests.get(f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={ticker}&outputsize=full&apikey={API_KEY}').json()
  return intraday


#convert the json data to a list
def json_to_list(json):
  symbol = json['Meta Data']['2. Symbol']
  data = json['Time Series (Daily)']
  data_list = []
  for date in data:
    fixedDate = datetime.datetime.strptime(date, '%Y-%m-%d').date()
    data_list.append([symbol, 
                      fixedDate, 
                      float(data[date]['1. open']), 
                      float(data[date]['2. high']), 
                      float(data[date]['3. low']), 
                      float(data[date]['4. close']), 
                      int(data[date]['5. volume'])
                      ])
  return data_list

