import pytest
from telesignenterprise.phoneid import PhoneIdClient

# Replace with actual credentials for successful test response
CUSTOMER_ID = "FFFFFFFF-EEEE-DDDD-1234-AB1234567890"
API_KEY = "ABC12345yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw=="

@pytest.fixture(scope="module")
def phoneid():
    return PhoneIdClient(CUSTOMER_ID, API_KEY,auth_method="Basic")

def test_phone_id_path(phoneid):
    phone_number = "11234567890"
    phone_id_response = phoneid.phone_id_path(phone_number)
    assert phone_id_response.ok, f"Failed to get PhoneID Path for {phone_id_response.json}"
    assert phone_id_response.json.get('status').get('description') == "Transaction successfully completed"

def test_phone_id_payload(phoneid):
    phone_number = "11234567890"
    phone_id_response = phoneid.phone_id_body(phone_number)
    assert phone_id_response.ok, f"Failed to get PhoneID Body for {phone_id_response.json}"
    assert phone_id_response.json.get('status').get('description') == "Transaction successfully completed"