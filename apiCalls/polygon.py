import requests
import os
import sqlite3
import datetime
from dotenv import load_dotenv
import database

def get_data(ticker):
  load_dotenv()
  API_KEY = os.getenv('API_KEY_POLYGON')
  intraday = requests.get(f'https://api.polygon.io/v2/aggs/ticker/VOO/range/1/day/2000-01-01/{datetime.today().strftime('%Y-%m-%d')}?adjusted=true&sort=asc&limit=50000&apiKey={API_KEY}').json()
  return intraday






#convert the json data to a list
def json_to_list(json):
  symbol = json['ticker']
  data = json['res']
  data_list = []
  for date in data:
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