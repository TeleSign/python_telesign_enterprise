from __future__ import print_function
from telesignenterprise.phoneid import PhoneIdClient

customer_id = "Put your Customer ID between these quotes."
api_key = "Put your API key between these quotes."

phone_number = "Put the phone number you want to retrieve consent history for between these quotes."
consent_method = "1"
consent_timestamp = "2019-07-12T02:39:27Z"

params = {"consent_method" : consent_method, "consent_timestamp" : consent_timestamp, "addons": {"contact" : {}}}
phoneid = PhoneIdClient(customer_id, api_key)

response = phoneid.consent_send(phone_number, **params)

print(response.json)

"""

This code sample shows you how to send consent for an add-on service.

"""
