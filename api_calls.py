import requests
import os
import sqlite3
from dotenv import load_dotenv

def get_data(ticker):
  load_dotenv()
  API_KEY = os.getenv('API_KEY')
  intraday = requests.get(f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={ticker}&outputsize=full&apikey={API_KEY}').json()
  return intraday

def save_data_to_database(json)

  pass

def create_database():
  conn = sqlite3.connect('historical.db')
  c = conn.cursor()
  c.execute('''CREATE TABLE IF NOT EXISTS stock_data (symbol text, date date, open real, high real, low real, close real, volume integer)''')
  conn.commit()
  conn.close()
  return