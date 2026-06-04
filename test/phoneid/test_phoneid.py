import pytest
from unittest.mock import patch, MagicMock
from telesignenterprise.phoneid import PhoneIdClient

@pytest.fixture
def phoneid():
    customer_id = "FFFFFFFF-EEEE-DDDD-1234-AB1234567890"
    api_key = "ABC12345yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw=="
    return PhoneIdClient(customer_id, api_key, auth_method="Basic")

def test_phoneid_standard(phoneid):
    phone_number = "11234567890"
    complete_phone_number = f"1{phone_number}"
    reference_id = "a" * 32
    
    with patch.object(PhoneIdClient, 'get') as mock_get:
        mock_response = MagicMock(
            ok=True,
            json={
                "reference_id": reference_id,
                "sub_resource": "standard",
                "status": {
                    "code": 300,
                    "description": "Transaction successfully completed"
                },
                "numbering": {
                    "original": {
                        "complete_phone_number": complete_phone_number,
                        "country_code": "1",
                        "phone_number": phone_number
                    }
                }
            },
        )
        mock_get.return_value = mock_response

        response = phoneid.standard(phone_number)

        mock_get.assert_called_once()
        called_url = mock_get.call_args[0][0]

        assert called_url == f"/v1/phoneid/standard/{phone_number}"
        assert response.ok
        assert response.json.get("reference_id") == reference_id
        assert response.json.get("status", {}).get("code") == 300
        assert response.json.get("numbering", {}).get("original", {}).get("complete_phone_number") == complete_phone_number


def test_phoneid_live(phoneid):
    phone_number = "11234567890"
    reference_id = "a" * 32
    ucid = "ATCK"

    with patch.object(PhoneIdClient, 'get') as mock_get:
        mock_response = MagicMock(
            ok=True,
            json={
                "reference_id": reference_id,
                "sub_resource": "live",
                "status": {
                    "code": 300,
                    "description": "Transaction successfully completed"
                },
                "live": {
                    "subscriber_status": "ACTIVE"
                }
            },
        )
        mock_get.return_value = mock_response

        response = phoneid.live(phone_number, ucid)

        mock_get.assert_called_once()
        called_url = mock_get.call_args[0][0]

        assert called_url == f"/v1/phoneid/live/{phone_number}"
        assert response.ok
        assert response.json.get("reference_id") == reference_id
        assert response.json.get("status", {}).get("code") == 300
        assert response.json.get("live", {}).get("subscriber_status") == "ACTIVE"

def test_phoneid_path(phoneid):
    phone_number = "11234567890"
    reference_id = "a" * 32

    with patch.object(PhoneIdClient, 'post') as mock_post:
        mock_response = MagicMock() 
        mock_response.ok = True
        mock_response.json = {"reference_id": reference_id}
        mock_post.return_value = mock_response

        response = phoneid.phone_id_path(phone_number)

        mock_post.assert_called_once()
        called_url = mock_post.call_args[0][0]
        called_json = mock_post.call_args[1]['consent']

        assert called_url == f"/v1/phoneid/{phone_number}"
        assert "method" in called_json
        assert called_json["method"] == 1
        assert response.ok
        assert response.json.get("reference_id") == reference_id


def test_phoneid_body(phoneid):
    phone_number = "11234567890"
    reference_id = "a" * 32

    with patch.object(PhoneIdClient, 'post') as mock_post:
        mock_response = MagicMock()
        mock_response.ok = True
        mock_response.json = {"reference_id": reference_id}
        mock_post.return_value = mock_response

        response = phoneid.phone_id_body(phone_number)

        mock_post.assert_called_once()
        called_url = mock_post.call_args[0][0]

        assert called_url == "/v1/phoneid"
        assert response.ok
        assert response.json.get("reference_id") == reference_id