# Use the Consent History feature of the PhoneID Consent API to retrieve
# the complete consent history for a phone number.
# You can specify the add-on(s) the consent history is for.

from __future__ import print_function
from telesignenterprise.phoneid import PhoneIdClient

customer_id = "Put your customer ID between these quotes."
api_key = "Put your API key between these quotes."

phone_number = "Put the complete phone number you want to retrieve the consent history for here."

phoneid = PhoneIdClient(customer_id, api_key)

response = phoneid.consent_history(phone_number)

print(response.json)
