# src/sql.py

import mysql.connector
from src.logger import logger

def create_db_connection(host: str, user: str, passwd: str, database: str, query: str):
    mydb = mysql.connector.connect(
        host=host,
        user=user,
        passwd=passwd,
        database=database
    )

    mycursor = mydb.cursor()
    mycursor.execute(query)
    my_result = mycursor.fetchall()
    result_string = ', '.join([str(item[0]) for item in my_result])
    logger.info(f'Got the results from SQL server {result_string}')
    return my_result

def fetch_columns(host: str, user: str, passwd: str, database: str, table_name: str):
    # SQL query to fetch column names
    query = f"DESCRIBE {table_name}"
    
    # Get the result from create_db_connection function
    columns = create_db_connection(host, user, passwd, database, query)
    
    # Extract column names from the result
    column_names = [column[0] for column in columns]
    logger.info(f'fetched columns from database')

    return column_names
