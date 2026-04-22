from __future__ import print_function
from telesignenterprise.messaging import MessagingClient

# In public or production environments, the credentials should not be hardcoded. 
# Environment variables can be used for sensitive data.
customer_id = "FFFFFFFF-EEEE-DDDD-1234-AB1234567890"
api_key = "ABC12345yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw=="

phone_number = "11234567890"
message = "You're scheduled for a dentist appointment at 2:30PM."
message_type = "ARN"

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
    print("Response body: {}".format(response.json))
except Exception as e:
    print("An error occurred: {}".format(e))