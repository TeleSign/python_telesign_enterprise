import pytest
from unittest.mock import patch, MagicMock
from telesignenterprise.verify import VerifyClient

@pytest.fixture
def verify():
    customer_id = "FFFFFFFF-EEEE-DDDD-1234-AB1234567890"
    api_key = "ABC12345yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw=="
    return VerifyClient(customer_id, api_key, auth_method="Basic")

def test_verify_sms(verify):
    phone_number = "11234567890"
    reference_id = "a" * 32

    with patch.object(VerifyClient, 'post') as mock_post:
        mock_response = MagicMock(
            ok=True,
            json={
                "reference_id": reference_id,
                "status": {
                    "code": 290,
                    "description": "Message in progress"
                },
                "verify": {
                    "code_state": "UNKNOWN",
                }
            },
        )
        mock_post.return_value = mock_response

        response = verify.sms(phone_number)

        mock_post.assert_called_once()
        called_url = mock_post.call_args[0][0]
        called_kwargs = mock_post.call_args[1]

        assert called_url == "/v1/verify/sms"
        assert called_kwargs.get("phone_number") == phone_number
        assert response.ok
        assert response.json.get("reference_id") == reference_id
        assert response.json.get("status", {}).get("code") == 290
        assert response.json.get("verify", {}).get("code_state") == "UNKNOWN"

def test_verify_voice(verify):
    phone_number = "11234567890"
    reference_id = "567A4C809E30060091D27AE21FFF0EC5"

    with patch.object(VerifyClient, 'post') as mock_post:
        mock_response = MagicMock(
            ok=True,
            json={
                "reference_id": reference_id,
                "status": {
                    "code": 130,
                    "description": "Call blocked by TeleSign"
                },
                "verify": {
                    "code_state": "UNKNOWN",
                }
            },
        )
        mock_post.return_value = mock_response

        response = verify.voice(phone_number)

        mock_post.assert_called_once()
        called_url = mock_post.call_args[0][0]
        called_kwargs = mock_post.call_args[1]

        assert called_url == "/v1/verify/call"
        assert called_kwargs.get("phone_number") == phone_number
        assert response.ok
        assert response.json.get("reference_id") == reference_id
        assert response.json.get("status", {}).get("code") == 130
        assert response.json.get("verify", {}).get("code_state") == "UNKNOWN"

def test_verify_smart(verify):
    phone_number = "11234567890"
    ucid = "ATCK"
    reference_id = "567A4C80AAC4010493818CBDC6DF97EA"

    with patch.object(VerifyClient, 'post') as mock_post:
        mock_response = MagicMock(
            ok=True,
            json={
                "reference_id": reference_id,
                "sub_resource": "sms",
                "status": {
                    "code": 290,
                    "description": "Message in progress"
                },
                "verify": {
                    "code_state": "UNKNOWN",
                }
            }
        )
        mock_post.return_value = mock_response

        response = verify.smart(phone_number, ucid)

        mock_post.assert_called_once()
        called_url = mock_post.call_args[0][0]
        called_kwargs = mock_post.call_args[1]

        assert called_url == "/v1/verify/smart"
        assert called_kwargs.get("phone_number") == phone_number
        assert called_kwargs.get("ucid") == ucid
        assert response.ok
        assert response.json.get("reference_id") == reference_id
        assert response.json.get("status", {}).get("code") == 290

def test_verify_status(verify):
    reference_id = "567A4C809E30060091D27AE21FFF0EC5"

    with patch.object(VerifyClient, 'get') as mock_get:
        mock_response = MagicMock(
            ok=True,
            json={
                "reference_id": reference_id,
                "sub_resource": "call",
                "status": {
                    "code": 130,
                    "description": "Call blocked by TeleSign"
                },
                "verify": {
                    "code_state": "UNKNOWN",
                }
            }
        )
        mock_get.return_value = mock_response

        response = verify.status(reference_id)

        mock_get.assert_called_once()
        called_url = mock_get.call_args[0][0]

        assert called_url == f"/v1/verify/{reference_id}"
        assert response.ok
        assert response.json.get("reference_id") == reference_id
        assert response.json.get("status", {}).get("code") == 130
        assert response.json.get("verify", {}).get("code_state") == "UNKNOWN"

def test_verify_completion(verify):
    reference_id = "567A4C809E30060091D27AE21FFF0EC5"

    with patch.object(VerifyClient, 'put') as mock_put:
        mock_response = MagicMock(
            ok=True,
            json={
                "reference_id": reference_id,
                "status": {
                    "code": 1900,
                    "description": "Verify completion successfully recorded"
                }
            }
        )
        mock_put.return_value = mock_response

        response = verify.completion(reference_id)

        mock_put.assert_called_once()
        called_url = mock_put.call_args[0][0]

        assert called_url == f"/v1/verify/completion/{reference_id}"
        assert response.ok
        assert response.json.get("reference_id") == reference_id
        assert response.json.get("status", {}).get("code") == 1900
        assert response.json.get("status", {}).get("description") == "Verify completion successfully recorded"

def test_verify_create_verification_process(verify):
    phone_number = "11234567890"
    reference_id = "667A4C80C99801509332FC4474EF3986"

    with patch.object(verify.omniverify, 'createVerificationProcess') as mock_create:
        mock_response = MagicMock(
            ok=True,
            json={
                "reference_id": reference_id,
                "recipient": {
                    "phone_number": phone_number
                },
                "state": "CREATED",
                "status": {
                    "code": 3901,
                    "description": "Request in progress"
                }
            }
        )
        mock_create.return_value = mock_response

        params = {"channel": "sms"}
        response = verify.createVerificationProcess(phone_number, params)

        mock_create.assert_called_once_with(phone_number, params)
        assert response.ok
        assert response.json.get("reference_id") == reference_id
        assert response.json.get("state") == "CREATED"
        assert response.json.get("status", {}).get("code") == 3901
