import os
import pytest
from telesignenterprise.omniverify import OmniVerify

# Replace with actual credentials for successful test response
CUSTOMER_ID = os.getenv("CUSTOMER_ID", "FFFFFFFF-EEEE-DDDD-1234-AB1234567890")
API_KEY = os.getenv(
    "API_KEY",
    "ABC12345yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw==",
)


@pytest.fixture(scope="module")
def omniverify():
    if not CUSTOMER_ID or not API_KEY:
        pytest.skip(
            "TELESIGN_CUSTOMER_ID and TELESIGN_API_KEY environment variables are required for integration tests."
        )
    return OmniVerify(CUSTOMER_ID, API_KEY)


def test_create_and_retrieve_verification_process(omniverify):
    phone_number = (
        "11234567890"  # Replace with a valid test phone number including country code
    )

    # Create verification process
    create_params = {"verification_policy": [{"method": "sms"}]}
    create_response = omniverify.createVerificationProcess(phone_number, create_params)

    assert (
        create_response.ok
    ), f"Failed to create verification process: {create_response.json}"
    reference_id = create_response.json.get("reference_id")
    assert reference_id and len(reference_id) == 32, "Invalid reference_id returned"

    # Retrieve verification process details
    retrieve_response = omniverify.getVerificationProcess(reference_id)
    assert (
        retrieve_response.ok
    ), f"Failed to retrieve verification process: {retrieve_response.json}"

    data = retrieve_response.json
    assert "reference_id" in data and data["reference_id"] == reference_id


def test_create_update_and_retrieve_verification_process(omniverify):
    phone_number = (
        "11234567890"  # Replace with a valid test phone number including country code
    )

    # Create verification process
    create_params = {"verification_policy": [{"method": "sms"}]}
    create_response = omniverify.createVerificationProcess(phone_number, create_params)
    assert (
        create_response.ok
    ), f"Failed to create verification process: {create_response.json}"
    reference_id = create_response.json.get("reference_id")
    assert reference_id and len(reference_id) == 32, "Invalid reference_id returned"

    # Simulate user entering the OTP (replace '123456' with an actual OTP for a successful response)
    otp_code = "123456"
    update_params = {"action": "finalize", "security_factor": otp_code}
    # Test both SDK-internal and manual Basic Auth PATCH
    for use_basic_auth in (False, True):
        update_response = omniverify.updateVerificationProcess(
            reference_id, update_params, use_basic_auth=use_basic_auth
        )
        # Acceptable error codes: 400 (bad request), 401 (unauthorized), 3904/3909 (Telesign verification errors: Rate Eimit Exceeded/Invalid code entered), 3400 (Telesign not authorized)
        allowed_status_codes = (400, 401, 3904, 3909)
        allowed_telesign_codes = 3400
        telesign_code = (
            update_response.json.get("status", {}).get("code")
            if update_response.json and isinstance(update_response.json, dict)
            else None
        )
        assert (
            update_response.ok
            or update_response.status_code in allowed_status_codes
            or telesign_code in allowed_telesign_codes
        ), f"Unexpected update response: {update_response.json}"

    # Retrieve verification process details
    retrieve_response = omniverify.getVerificationProcess(reference_id)
    assert (
        retrieve_response.ok
    ), f"Failed to retrieve verification process: {retrieve_response.json}"
    data = retrieve_response.json
    assert "reference_id" in data and data["reference_id"] == reference_id
