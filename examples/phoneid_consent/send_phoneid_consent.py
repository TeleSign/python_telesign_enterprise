# Use the Send feature of the PhoneID Consent API to send
# consent information for a phone number for one or more add-ons.

from __future__ import print_function
from telesignenterprise.phoneid import PhoneIdClient

customer_id = "Put your customer ID between these quotes."
api_key = "Put your API key between these quotes."

phone_number = "Put the complete phone number you want to send consent information for here."
consent_method = "1"
consent_timestamp = "2019-07-12T02:39:27Z"

params = {"consent_method" : consent_method, "consent_timestamp" : consent_timestamp, "addons": {"contact" : {}}}
phoneid = PhoneIdClient(customer_id, api_key)

response = phoneid.consent_send(phone_number, **params)

print(response.json)
