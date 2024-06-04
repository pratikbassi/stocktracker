import sqlite3

#create a database with appropriate columns
def create_database():
  conn = sqlite3.connect('historical.db')
  c = conn.cursor()
  c.execute('''CREATE TABLE IF NOT EXISTS stock_data (symbol text, date text, open text, high text, low text, close text, volume text)''')
  conn.commit()
  conn.close()
  return

#save the list data to the database
def save_data_to_database(data_list):
  conn = sqlite3.connect('historical.db')
  c = conn.cursor()
  c.executemany('INSERT INTO stock_data VALUES (?,?,?,?,?,?,?)', data_list)
  results = conn.commit()
  conn.close()
  return results