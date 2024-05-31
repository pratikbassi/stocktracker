import requests
import os
import sqlite3
from dotenv import load_dotenv

#create a database with appropriate columns
def create_database():
  conn = sqlite3.connect('historical.db')
  c = conn.cursor()
  c.execute('''CREATE TABLE IF NOT EXISTS stock_data (symbol text, date date, open real, high real, low real, close real, volume integer)''')
  conn.commit()
  conn.close()
  return

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
    data_list.append([symbol, date, data[date]['1. open'], data[date]['2. high'], data[date]['3. low'], data[date]['4. close'], data[date]['5. volume']])
  return data_list

#save the list data to the database
def save_data_to_database(data_list):
  conn = sqlite3.connect('historical.db')
  c = conn.cursor()
  c.executemany('INSERT INTO stock_data VALUES (?,?,?,?,?,?,?)', data_list)
  pass

#main function
def main():
  create_database()
  ticker = input("Enter the ticker symbol: ")
  data = get_data(ticker)
  data_list = json_to_list(data)
  save_data_to_database(data_list)
  return