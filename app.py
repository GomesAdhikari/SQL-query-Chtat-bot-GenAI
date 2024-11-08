from flask import Flask, render_template, request, redirect, session, jsonify
import mysql.connector
import src.gemini
import src.sql
from dotenv import load_dotenv
from src.logger import logger
# Initialize Flask app
app = Flask(__name__)

# Load environment variables
load_dotenv()
logger.info('Started flask Application')
# Secret key for session management
app.secret_key = 'your_secret_key'

@app.route('/', methods=['GET', 'POST'])
def setup():
    if request.method == 'POST':
        # Save connection details to session
        session['host'] = request.form['host']
        session['user'] = request.form['user']
        session['passwd'] = request.form['passwd']
        session['database'] = request.form['database']
        session['table_name'] = request.form['table_name']
        
        # Redirect to the chat page after setup
        return redirect('/chat')
    
    return render_template('setup.html')

@app.route('/chat', methods=['GET', 'POST'])
def chat():
    if request.method == 'POST':
        # Get the message from the user input
        message = request.form['message']
        
        # Retrieve database connection details from session
        host = session.get('host')
        user = session.get('user')
        passwd = session.get('passwd')
        database = session.get('database')
        table_name = session.get('table_name')

        # Fetch columns from the table
        columns = src.sql.fetch_columns(host, user, passwd, database, table_name)
        logger.info(f'Created connection with host - {host}| user - {user} | password - {passwd} | database - {database} |')
        logger.info('Started fetching columns from DataBase')

        # Generate SQL query using Gemini
        sql_query, question = src.gemini.get_query(table_name, columns, message)
        
        # Clean up the SQL query
        sql_query = sql_query.replace('```sql', '').replace('```', '').strip()

        # Execute the SQL query and get the response
        response = src.sql.create_db_connection(host, user, passwd, database, sql_query)

        # Get insights from the Gemini API
        message_response = src.gemini.message_user(response, question)

        return jsonify({'response': message_response})

    return render_template('chat.html')

if __name__ == '__main__':
    app.run(debug=True)
