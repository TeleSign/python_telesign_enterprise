from __future__ import print_function
from telesignenterprise.appverify import AppVerifyClient


customer_id = "FFFFFFFF-EEEE-DDDD-1234-AB1234567890"
api_key = "EXAMPLE----TE8sTgg45yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw=="
phone_number = "phone_number"

verify = AppVerifyClient(customer_id, api_key)

# Initiate App Verify Call
initiate_response = verify.initiate(phone_number)
print("initiate response: {}\n".format(initiate_response.json))

# Get intermediate call status to trigger a failure or retry quickly on the mobile app
reference_id = initiate_response.json['reference_id']
status_response = verify.status(reference_id)
print("initiate response: {}\n".format(status_response.json))

# Finalize App Verify Transaction
verify_code = raw_input("Please enter the verification code from the caller id: ")
finalize_response = verify.finalize(reference_id, verify_code=verify_code)
print("\nfinalize response: {}\n".format(finalize_response.json))
