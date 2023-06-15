import os
from twilio.rest import Client

 

# Your Account SID and Auth Token from console.twilio.com

account_sid = "AC056ac8960010bea0a800750bb945c8b7"
api_key= "SKf566a2a411d40db5d94219d27a505db1"
api_secret= "bIgHJsquuIJUgUWsayVOOINaRkuzCGo2"

client = Client(api_key, api_secret, account_sid)
accounts= client.api.v2010.accounts.list(limit=20)

for record in accounts:
    print(record.sid)

message= client.messages.create(
    from_='whatsapp:+14155238886',
    body='hola',
    to='whatsapp:+573175127124'
)

print(message.sid)