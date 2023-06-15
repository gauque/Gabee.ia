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

#def load_data_excel(file_path: str) -> pd.DataFrame:
"""
    Load data from a CSV file and return a pandas DataFrame object.
    Parameters:
        file_path: str - the file path to the Excel file containing the data.
    Returns:
        pd.DataFrame - the loaded data as a pandas DataFrame object.
    """
    #df = pd.read_excel(file_path)

    #return df

#df = load_data_excel(r"C:\Users\gauquebauz001\Downloads\Ventas_Proyectos_BU (2).xlsx")
#df['Año-Mes_Date'] = pd.to_datetime(df['Año-Mes'], format='%Y-%m')
#df.head(3)


#Create an array with the colors you want to use
#colors = ["#D04A02", "#EB8C00","#FFB600", "#D93954" , "#E0301E","#933401","#AE6800", "#714300","#855F00", "#6E2A35","#741910"]
#Set your custom color palette
#sns.set_palette(sns.color_palette(colors))



#Definición Función: cumplimiento de presupuesto por BU
#def cumplimiento_presupuesto_BU (df, BU,mes_inicial,año_inicial,mes_final,año_final):

       
    #Fecha_inicial = pd.to_datetime(str(año_inicial)+'-'+ str(mes_inicial), format='%Y-%m')
    #Fecha_final = pd.to_datetime(str(año_final)+'-'+ str(mes_final), format='%Y-%m')

   #Se filtran los datos del dataframe
    #df_cumplimiento_presupuesto_BU = df[['Nombre_BU','Año-Mes','Año-Mes_Date','Valor_Proyecto','Presupuesto_mensual_BU']].copy()
    #df_cumplimiento_presupuesto_BU = df_cumplimiento_presupuesto_BU[df_cumplimiento_presupuesto_BU['Nombre_BU']==BU].copy()
    #df_cumplimiento_presupuesto_BU = df_cumplimiento_presupuesto_BU[df_cumplimiento_presupuesto_BU['Año-Mes_Date']>=Fecha_inicial].copy()
    #df_cumplimiento_presupuesto_BU = df_cumplimiento_presupuesto_BU[df_cumplimiento_presupuesto_BU['Año-Mes_Date']<=Fecha_final].copy()

    #df_cumplimiento_presupuesto_BU = pd.melt(df_cumplimiento_presupuesto_BU, id_vars=['Nombre_BU','Año-Mes','Año-Mes_Date'],value_vars=['Valor_Proyecto','Presupuesto_mensual_BU'] ).copy()
    #df_cumplimiento_presupuesto_BU_proyecto = df_cumplimiento_presupuesto_BU[df_cumplimiento_presupuesto_BU['variable']=='Valor_Proyecto'].groupby(by=['Nombre_BU','Año-Mes','Año-Mes_Date','variable']).sum().reset_index().copy()

    #df_cumplimiento_presupuesto_BU_presupuesto = df_cumplimiento_presupuesto_BU[df_cumplimiento_presupuesto_BU['variable']=='Presupuesto_mensual_BU'].groupby(by=['Nombre_BU','Año-Mes','Año-Mes_Date','variable']).first().reset_index().copy()

    #df_cumplimiento_presupuesto_BU = pd.concat([df_cumplimiento_presupuesto_BU_proyecto,df_cumplimiento_presupuesto_BU_presupuesto]).copy()

    #df_cumplimiento_presupuesto_BU.rename(columns={"variable": "Tipo de Valor"},inplace=True)
    #df_cumplimiento_presupuesto_BU.replace({"Valor_Proyecto": "WIP", "Presupuesto_mensual_BU": "Presupuesto"}, inplace=True)

    #fig, ax = plt.subplots()
    #fig.set_size_inches(8,6)
    #sns.barplot(x=df_cumplimiento_presupuesto_BU["Año-Mes"],y= df_cumplimiento_presupuesto_BU["value"],hue = df_cumplimiento_presupuesto_BU["Tipo de Valor"] ,errorbar= None )

    #plt.title(f'Cumplimiento de Presupuesto de {BU}')
    #plt.xlabel('Mes')
    #plt.ylabel('Valor (Millones de COP)')

    #img_Cumplimiento = plt.savefig('cumplimiento_presupuesto_BU.jpg',bbox_inches='tight', pad_inches=0.2)

    #plt.show()

    #return img_Cumplimiento

# Definición de Variables
#BU_filtro_Cump_Pres_BU = 'ANALIT'
#mes_inicial_Cump_Pres_BU = 1
#año_inicial_Cump_Pres_BU = 2023
#mes_final_Cump_Pres_BU = 4
#año_final_Cump_Pres_BU = 2023

# Ejecución de función: 
#cumplimiento_presupuesto_BU(df,BU_filtro_Cump_Pres_BU,mes_inicial_Cump_Pres_BU,año_inicial_Cump_Pres_BU,mes_final_Cump_Pres_BU,año_final_Cump_Pres_BU )

#def descubrimiento_Cartera_BU (df, BU):

    # Se filtran los datos del dataframe
    #df_Descubrimiento_Cartera_BU = df[df['Nombre_BU']==BU].copy()
    #df_Descubrimiento_Cartera_BU = df_Descubrimiento_Cartera_BU[['Project Name','Manager ID','Valor_Proyecto','Cartera_30','Cartera_90','Cartera_+90']].copy()
    #df_Descubrimiento_Cartera_BU = df_Descubrimiento_Cartera_BU[df_Descubrimiento_Cartera_BU['Cartera_30']>0]

    #df_Descubrimiento_Cartera_BU = df_Descubrimiento_Cartera_BU['Cartera_30']

    #df_Descubrimiento_Cartera_BU = df_Descubrimiento_Cartera_BU.round(1)

    #df_Descubrimiento_Cartera_BU.rename(columns={"Project Name": "Proyecto", "Manager ID": "Gerente", "Valor_Proyecto": "Valor del Proyecto", "Cartera_30": "Cartera 30-60 días" , "Cartera_90": "Cartera 60-90 días" , "Cartera_+90": "Cartera mas 90 días"},inplace=True)
    #fig, ax = plt.subplots(figsize=(4, ((len(df_Descubrimiento_Cartera_BU)+1)/4)+0.4)) # set size frame
    #ax.xaxis.set_visible(False)  # hide the x axis
    #ax.yaxis.set_visible(False)  # hide the y axis
    #ax.set_frame_on(False)  # no visible frame, uncomment if size is ok
    #tabla = table(ax, df_Descubrimiento_Cartera_BU, loc='upper right', colWidths=[0.17]*len(df_Descubrimiento_Cartera_BU.columns))  # where df is your data frame
    #tabla.auto_set_font_size(False) # Activate set fontsize manually
    #tabla.set_fontsize(12) # if ++fontsize is necessary ++colWidths
    #tabla.scale(1.8, 2) # change size table
    #plt.title(f'Estado de cartera de {BU} - Valores Millones COP     ', loc = 'left')
    
    #img_Cartera = plt.savefig('Descubrimiento_cartera.jpg', bbox_inches='tight', pad_inches=0.2)

    #return img_Cartera

   #Definición de Variables
   
   
#BU_filtro_Cump_Pres_BU = 'ANALIT'

   #Ejecución de función: 
#descubrimiento_Cartera_BU(df,BU_filtro_Cump_Pres_BU )

#def func_porcentajes(pct, allvals):
    #absolute = int(pct/100.*np.sum(allvals))
    #return "{:.1f}%\n({:d} Mill COP)".format(pct, absolute)

#def porcentaje_cartera_BU (df, BU ):

    # Se filtran los datos del dataframe
    #df_porcentaje_cartera_BU = df[df['Nombre_BU']==BU].copy()
    #df_porcentaje_cartera_BU = df_porcentaje_cartera_BU[['Project Name','Manager ID','Cartera_30','Cartera_90','Cartera_+90']].copy()
    #df_porcentaje_cartera_BU = df_porcentaje_cartera_BU[df_porcentaje_cartera_BU['Cartera_30']>0]

    #df_porcentaje_cartera_BU = df_porcentaje_cartera_BU.round(1)

    #df_porcentaje_cartera_BU.rename(columns={"Project Name": "Proyecto", "Manager ID": "Gerente", "Valor_Proyecto": "Valor del Proyecto", "Cartera_30": "Cartera 30-60 días" , "Cartera_90": "Cartera 60-90 días" , "Cartera_+90": "Cartera mas 90 días"},inplace=True)

    #df_porcentaje_cartera_BU = df_porcentaje_cartera_BU.head(6).copy()

    #fig, ax = plt.subplots()
    #fig.set_size_inches(8,6)

    #ax.pie(df_porcentaje_cartera_BU["Cartera 30-60 días"],labels = df_porcentaje_cartera_BU["Proyecto"],  autopct = lambda pct: func_porcentajes(pct, df_porcentaje_cartera_BU["Cartera 30-60 días"]) ,  startangle=90)
    #ax.axis('equal') 
    #plt.barplot(x=df_cumplimiento_presupuesto_BU["Año-Mes"],y= df_cumplimiento_presupuesto_BU["value"],hue = df_cumplimiento_presupuesto_BU["Tipo de Valor"] ,errorbar= None )

    #plt.title(f'Distribución de cartera de {BU}')


    #img = plt.savefig('Porcentaje_cartera_BU.jpg',bbox_inches='tight', pad_inches=0.2)

    #plt.show()

    #return img


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
