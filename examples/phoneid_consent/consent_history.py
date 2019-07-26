from __future__ import print_function
from telesignenterprise.phoneid import PhoneIdClient

customer_id = "Put your Customer ID between these quotes."
api_key = "Put your API key between these quotes."

phone_number = "Put the phone number you want to retrieve consent history for between these quotes."

phoneid = PhoneIdClient(customer_id, api_key)

response = phoneid.consent_history(phone_number)

print(response.json)

"""
This sample code shows how to retrieve consent history for a phone number.
"""
