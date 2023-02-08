from twilio.rest import Client

# Your Twilio Account SID and Auth Token

account_sid = 'Your Twilio Account SID'

auth_token = 'Your Twilio Auth Token'

client = Client(account_sid, auth_token)

# The phone number you wish to send and receive texts from

from_whatsapp_number = 'whatsapp:+14155238886'

to_whatsapp_number = 'whatsapp:+12345678901'

# The message you want to send as an autoreply

autoreply_message = 'I am Busy right now , i will text you soon Buddy'

# Send an autoreply message

message = client.messages.create(

    to=to_whatsapp_number,

    from_=from_whatsapp_number,

    body=autoreply_messag

)

print(message.sid)

