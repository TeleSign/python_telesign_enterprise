from __future__ import print_function
from telesignenterprise.omniverify import OmniVerify
import json

customer_id = "FFFFFFFF-EEEE-DDDD-1234-AB1234567890"
api_key = "EXAMPLE----TE8sTgg45yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw=="

phone_number = input("Please enter the phone number (with country code, digits only): ").strip()
if not phone_number.isdigit():
    print("Error: phone number must contain digits only.")
    exit(1)

omniverify = OmniVerify(customer_id, api_key)

# Create the verification process
create_params = {
    "verification_policy": [{"method": "sms"}]
}
create_response = omniverify.createVerificationProcess(phone_number, create_params)

if create_response.ok:
    reference_id = create_response.json.get("reference_id")
    print("Verification process created successfully.")
    print("Reference ID:", reference_id)
else:
    print("Failed to create verification process.")
    print("Status code:", create_response.status_code)
    print("Response:", create_response.json)
    exit(1)

# Prompt for OTP (security factor) and update the verification process
security_factor = input("Please enter the OTP (security factor) to finalize the verification: ").strip()

update_params = {
    "action": "finalize",
    "security_factor": security_factor
}
update_response = omniverify.updateVerificationProcess(reference_id, update_params)

if update_response.ok:
    print("Verification process updated successfully.")
    print("Response:")
    print(json.dumps(update_response.json, indent=4))
else:
    print("Failed to update verification process.")
    print("Status code:", update_response.status_code)
    print("Response:", update_response.json)