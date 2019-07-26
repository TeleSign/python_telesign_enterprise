from __future__ import print_function
from telesignenterprise.phoneid import PhoneIdClient

customer_id = "Put your Customer ID between these quotes."
api_key = "Put your API key between these quotes."

phone_number = "Put the phone number you want to retrieve consent history for between these quotes."
consent_method = "1"

params = {"consent_method" : consent_method, "addons": {"contact" : {}}}
phoneid = PhoneIdClient(customer_id, api_key)

response = phoneid.consent_search(phone_number, **params)

print(response.json)

"""

This sample code shows you how to search for consent information for an add-on and type of consent that you specify. 

"""
