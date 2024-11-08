import os
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()
from src.logger import logger
# Configure Gemini API with the API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-pro')

def get_query(tablename,colunms,query):

    prompt = f'i have columns {colunms} in my database table{tablename} my query is{query} there should only be sql command no extra text.'
    response = model.generate_content(prompt)
    text_response = str(response.text)

    logger.info('Recorded query from API')

    return text_response,query

def message_user(response,query):
    
    prompt = f"this is my sql response{response} give me a message as if your are sql you are speaking to me and message must be precise and small no extra text because i am  sending this response directly somewhere response should not include sure this is your nswers etc only the answer text this was my question{query} and if my query is out of any sql question do not answer just say i cant answer to this question"
    response = model.generate_content(prompt)
    text_response = str(response.text)

    logger.info('Got the finl message from the API')
    
    return text_response