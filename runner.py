import sqlite3
import requests
import logging
import os

num_quotes_in_db = 10
log_to_file = True
log_location = "chuck_logs.log"
db_location = "quotes.db"

logger = logging.getLogger(str(os.getpid()))
if log_to_file:
    logging.basicConfig(format=f'%(asctime)s: [%(name)s] %(message)s', datefmt='%d/%m/%y %H:%M:%S',
                        filename=log_location, level=logging.INFO)
else:
    logging.NullHandler()

db_connection = sqlite3.connect(db_location)
with db_connection:
    cursor = db_connection.cursor()
    cursor.execute("CREATE table IF NOT EXISTS quotes (quote text)")
    cursor.execute("SELECT * FROM quotes")
    quotes_list = cursor.fetchall()

    quotes_list = quotes_list if quotes_list else []
    new_entries = []

    if num_quotes_in_db - len(quotes_list) > 0:
        logger.info(f"Retrieving {num_quotes_in_db - len(quotes_list)} new quote{'s' if num_quotes_in_db - len(quotes_list) > 1 else ''}")
        while len(quotes_list) + len(new_entries) < num_quotes_in_db:
            try:
                new_quote = requests.get("https://api.chucknorris.io/jokes/random").json()["value"]
            except requests.ConnectionError as error_message:
                logger.critical(error_message)
            new_entries.append((new_quote,))

        cursor.executemany("INSERT INTO quotes VALUES (?)", new_entries)
        logger.info(f"{len(new_entries)} quote{'s' if len(new_entries) > 1 else ''} added to database")

db_connection.close()
