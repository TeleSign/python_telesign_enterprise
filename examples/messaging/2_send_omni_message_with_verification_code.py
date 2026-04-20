from __future__ import print_function
import random
from telesignenterprise.messaging import MessagingClient

# In public or production environments, the credentials should not be hardcoded. 
# Environment variables can be used for sensitive data.
customer_id = "FFFFFFFF-EEEE-DDDD-1234-AB1234567890"
api_key = "ABC12345yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw=="

phone_number = "11234567890"
verify_code = str(random.randint(10000, 99999))
message = "Your code is {}".format(verify_code)
message_type = "OTP"

messaging = MessagingClient(customer_id, api_key)

params = {
    "message": { "sms": {
            "parameters": { "text": message },
            "template": "text"
        } },
    "message_type": message_type,
    "phone_number": phone_number,
    "channels": [
        {
            "channel": "sms",
            "fallback_time": 300
        }
    ]
}

try:
    response = messaging.omniMessage(params)
    print("Response status: {}".format(response.status_code))
except Exception as e:
    print("An error occurred: {}".format(e))
    exit(1)

user_entered_verify_code = input("Please enter the verification code you were sent: ")

if verify_code == user_entered_verify_code.strip():
    print("Your code is correct.")
else:
    print("Your code is incorrect.")