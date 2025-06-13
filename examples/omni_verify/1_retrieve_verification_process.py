from __future__ import print_function
from telesignenterprise.omniverify import OmniVerify
import json

customer_id = "FFFFFFFF-EEEE-DDDD-1234-AB1234567890"
api_key = "EXAMPLE----TE8sTgg45yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw=="

phone_number = input("Please enter the phone number (with country code, digits only): ").strip()
if not phone_number.isdigit():
    print("Error: phone number must contain digits only.")
else:
    omniverify = OmniVerify(customer_id, api_key)

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

    retrieve = input("Do you want to retrieve the verification process details now? (y/n): ").strip().lower()
    if retrieve == 'y':
        retrieve_response = omniverify.getVerificationProcess(reference_id)
        if retrieve_response.ok:
            print("Verification process details:")
            print(json.dumps(retrieve_response.json, indent=4))
        else:
            print("Failed to retrieve verification process.")
            print("Status code:", retrieve_response.status_code)
            print("Response:", retrieve_response.json)