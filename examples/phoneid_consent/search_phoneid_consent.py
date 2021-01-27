# Use the Search feature of the PhoneID Consent API to retrieve
# specific consent information about a phone number.
# You can specify the add-on(s) the consent information is for.

from __future__ import print_function
from telesignenterprise.phoneid import PhoneIdClient

customer_id = "Put your customer ID between these quotes."
api_key = "Put your API key between these quotes."

phone_number = "Put the complete phone number you want to retrieve specific consent history information for here."
consent_method = "1"

params = {"consent_method" : consent_method, "addons": {"contact" : {}}}
phoneid = PhoneIdClient(customer_id, api_key)

response = phoneid.consent_search(phone_number, **params)

print(response.json)
