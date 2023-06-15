# import flask dependencies
import flask
from flask import Flask
from flask import request, jsonify
import os
import google.cloud.dialogflow_v2beta1 as dialogflow
import requests
from twilio.rest import Client
import random
#import pandas as pd
#import seaborn as sns
#import matplotlib.pyplot as plt
#from pandas.plotting import table
#import numpy as np
import base64
import mimetypes
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'key.json'

DIALOGFLOW_PROJECT_ID ='asistentecomercial-fnia'
DIALOGFLOW_LANGUAGE_CODE = 'es'
SESSION_ID = 'me'

# initialize the flask appp
app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def root():
    return "Hello mi gente linda"

@app.route('/api/getMessage', methods=['GET', 'POST'])
def home():
   message=request.form.get('Body') #Get message from the user
   mobnum=request.form.get('From') #Who is the user (phone)
   #Create and configure Dialogflow Session
   session_client = dialogflow.SessionsClient() 
   session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)
   text_input = dialogflow.types.TextInput(text=message, language_code=DIALOGFLOW_LANGUAGE_CODE)
   query_input = dialogflow.types.QueryInput(text=text_input)
   try:
      response = session_client.detect_intent(session=session, query_input=query_input)
   except dialogflow.exceptions.InvalidArgument as e:
      raise
 
   print ("Query text:", response.query_result.query_text)
   print("Detected intent:", response.query_result.intent.display_name)
   print("Detected intent confidence", response.query_result.intent_detection_confidence)
   print("Fullfilment text:", response.query_result.fulfillment_text)

   intent_name = response.query_result.intent.display_name
   # Define a dictionary to map intent names to media URLs
   intent_media_map = {
       'Presupuesto - ANALIT - Grafica': 'https://pbs.twimg.com/media/FvQATbiXgAI456d?format=jpg&name=900x900',
       'Presupuesto - ANALIT - CART': 'https://pbs.twimg.com/media/FvQAfcbWAAES8en?format=jpg&name=900x900',
       'Presupuesto - ANALIT - CART - PIE': 'https://pbs.twimg.com/media/FvQAZSpWwAIC_pJ?format=jpg&name=900x900'
   }
   # Get the media URL corresponding to the intent
   media_url = intent_media_map.get(intent_name)
   # If a media URL was found, add it to the message kwargs
   if media_url:
       message_kwargs = {
           'from_': 'whatsapp:+14155238886',
           'body': response.query_result.fulfillment_text,
           'to': mobnum,
           'media_url': [media_url]
       }
   else:
       message_kwargs = {
           'from_': 'whatsapp:+14155238886',
           'body': response.query_result.fulfillment_text,
           'to': mobnum
       }

   account_sid = 'AC056ac8960010bea0a800750bb945c8b7'
   auth_token= '4f2f6b66579e33b089ef8f6c699e4cee'
   client=Client(account_sid, auth_token)
   message2 = client.messages.create(**message_kwargs)
   print(message2.sid)

# run the app
if __name__ == '__main__':
    app.run(debug=True, port=5500)
