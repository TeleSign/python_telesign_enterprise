import pytest
from unittest.mock import patch, MagicMock
from telesignenterprise.omniverify import OmniVerify

@pytest.fixture
def omniverify():
    customer_id = "FFFFFFFF-EEEE-DDDD-1234-AB1234567890"
    api_key = "EXAMPLE----TE8sTgg45yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw=="
    return OmniVerify(customer_id, api_key)

def test_create_verification_process_success(omniverify):
    phone_number = "11234567890"
    reference_id = "a" * 32

    with patch.object(OmniVerify, 'post') as mock_post:
        mock_response = MagicMock()
        mock_response.ok = True
        mock_response.json = {"reference_id": reference_id}
        mock_post.return_value = mock_response

        params = {"verification_policy": [{"method": "sms"}]}
        response = omniverify.createVerificationProcess(phone_number, params)

        mock_post.assert_called_once()
        called_url = mock_post.call_args[0][0]
        called_json = mock_post.call_args[1]['json_fields']

        assert called_url == "/verification"
        assert "recipient" in called_json
        assert called_json["recipient"]["phone_number"] == phone_number
        assert response.ok
        assert response.json["reference_id"] == reference_id

def test_get_verification_process_success(omniverify):
    reference_id = "a" * 32

    with patch.object(OmniVerify, 'get') as mock_get:
        mock_response = MagicMock()
        mock_response.ok = True
        mock_response.json = {"status": "completed"}
        mock_get.return_value = mock_response

        response = omniverify.getVerificationProcess(reference_id)

        mock_get.assert_called_once()
        called_url = mock_get.call_args[0][0]

        assert called_url == f"/verification/{reference_id}"
        assert response.ok
        assert response.json["status"] == "completed"

def test_get_verification_process_invalid_reference_id(omniverify):
    invalid_reference_id = "invalid_id"
    
    with patch.object(OmniVerify, 'get') as mock_get:
        mock_response = MagicMock()
        mock_response.ok = False
        mock_response.status_code = 400
        mock_response.json = {"status": {"code": 3400, "description": "Invalid reference_id format"}}
        mock_get.return_value = mock_response

        response = omniverify.getVerificationProcess(invalid_reference_id)
        
        mock_get.assert_called_once()
        called_url = mock_get.call_args[0][0]
        
        assert called_url == f"/verification/{invalid_reference_id}"
        assert not response.ok
        assert response.status_code == 400
        assert response.json["status"]["code"] == 3400

def test_update_verification_process_success(omniverify):
    reference_id = "a" * 32
    params = {
        "action": "finalize",
        "security_factor": "123456"
    }

    with patch.object(OmniVerify, 'patch') as mock_patch:
        mock_response = MagicMock()
        mock_response.ok = True
        mock_response.json = {
            "status": {"code": 3900, "description": "Verified"},
            "reference_id": reference_id
        }
        mock_patch.return_value = mock_response

        response = omniverify.updateVerificationProcess(reference_id, params)

        mock_patch.assert_called_once()
        called_url = mock_patch.call_args[0][0]
        called_json = mock_patch.call_args[1]['json_fields']

        assert called_url == f"/verification/{reference_id}/state"
        assert called_json["action"] == "finalize"
        assert called_json["security_factor"] == "123456"
        assert response.ok
        assert response.json["status"]["code"] == 3900

def test_update_verification_process_invalid_code(omniverify):
    reference_id = "a" * 32
    params = {
        "action": "finalize",
        "security_factor": "wrongcode"
    }

    with patch.object(OmniVerify, 'patch') as mock_patch:
        mock_response = MagicMock()
        mock_response.ok = False
        mock_response.status_code = 400
        mock_response.json = {
            "status": {"code": 3904, "description": "Verification Failed"}
        }
        mock_patch.return_value = mock_response

        response = omniverify.updateVerificationProcess(reference_id, params)

        mock_patch.assert_called_once()
        assert not response.ok
        assert response.status_code == 400
        assert response.json["status"]["code"] == 3904        