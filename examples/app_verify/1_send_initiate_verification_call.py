from __future__ import print_function
from telesignenterprise.appverify import AppVerifyClient


customer_id = "FFFFFFFF-EEEE-DDDD-1234-AB1234567890"
api_key = "ABC12345yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw=="
phone_number = "11234567890"

verify = AppVerifyClient(customer_id, api_key)

# Initiate App Verify Call
initiate_response = verify.initiate(phone_number)
print("initiate response: {}\n".format(initiate_response.json))
reference_id = initiate_response.json['reference_id']
print("Reference ID: ",reference_id)
status_response = verify.status(reference_id)
print(f"Status Code: {status_response.status_code if hasattr(status_response, 'status_code') else 'Unknown'}")
print("Status: ", format(status_response.json['status']['description']))