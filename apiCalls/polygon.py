import requests
import os
import sqlite3
import datetime
from dateutil.relativedelta import relativedelta
from dotenv import load_dotenv
import database

def get_data(ticker):
  load_dotenv()
  API_KEY = os.getenv('API_KEY_POLYGON')
  start_date = (datetime.datetime.now() - relativedelta(years=2)).strftime('%Y-%m-%d')
  intraday = requests.get(f'https://api.polygon.io/v2/aggs/ticker/AAPL/range/1/day/2023-01-09/2023-01-09?adjusted=true&sort=asc&apiKey=K6TFcVCi1pOosY6zM__lgQD11rWsT0uV').json()
  return intraday



#convert the json data to a list
def json_to_list(json):
  symbol = json['ticker']
  data = json['results']
  data_list = []
  for tick in data:
    fixedDate = datetime.datetime.strptime(date, '%Y-%m-%d').date()
    data_list.append([symbol, 
                      fixedDate, 
                      float(data[date]['o']), 
                      float(data[date]['h']), 
                      float(data[date]['l']), 
                      float(data[date]['c']), 
                      int(data[date]['v'])
                      ])
  return data_list


def run(ticker):
  data = get_data(ticker)
  data_list = json_to_list(data)
  database.create_database()
  results = database.save_data_to_database(data_list)
  return results