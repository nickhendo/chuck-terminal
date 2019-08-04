import sqlite3
import requests
import logging
import datetime
import os

logger = logging.basicConfig(filename="chuck_logs.log", level=logging.DEBUG)
db_connection = sqlite3.connect("quotes.db")
cursor = db_connection.cursor()

num_rows = 10

cursor.execute("CREATE table IF NOT EXISTS quotes (date text, quote text)")

cursor.execute("SELECT * FROM quotes")
quotes_list = cursor.fetchall()
trys = 0
new_entries = []
logger.
while len(quotes_list) + len(new_entries) < num_rows and trys < 5:
    new_quote = requests.get("https://api.chucknorris.io/jokes/random").json()["value"]
    trys += 1
    new_entries.append((datetime.datetime.now().date(), new_quote))
if new_entries:
    cursor.executemany("INSERT INTO quotes VALUES (?, ?)", new_entries)

db_connection.commit()
db_connection.close()
