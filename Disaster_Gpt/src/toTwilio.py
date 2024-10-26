""" Sends user data to Twilio which will send an SMS to users' phone number. """

import HelperFunctions

from twilio.rest import Client

account_sid = 'User'
auth_token = 'user'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='+14082170234',
  body='Natural Disaster Tech Support. \n'
       'Respond 1 to not get updates',
  to='+14378188822'
)

print(message.sid)

account_sid = 'user'
auth_token = 'user'
client = Client(account_sid, auth_token)

message2 = client.messages.create(
  from_='+14082170234',
  body=HelperFunctions.situation_message(),
  to='+14378188822'
)

print(message2.sid)
