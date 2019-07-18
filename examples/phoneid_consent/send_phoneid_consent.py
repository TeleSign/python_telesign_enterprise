from __future__ import print_function
from telesignenterprise.phoneid import PhoneIdClient

customer_id = "886481A0-DCBA-486C-A968-BAD1E8A7A7AF"
api_key = "kwxpgPzbqEsh2V1hw4XdKWpm51H5Modccwqn7MZD4yO7otnqjmx1ofotwbZT1DWaOrnbKWN32v4DwR7WQua6cw=="

phone_number = "your phone number here"
consent_method = "1"
consent_timestamp = "2019-07-12"

params = {"consent_method" : consent_method, "consent_timestamp" : consent_timestamp, "addons": {"contact" : {}}}
phoneid = PhoneIdClient(customer_id, api_key)

response = phoneid.consent(phone_number, **params)

print(response.json)
