import pytest
from unittest.mock import patch, MagicMock
from telesignenterprise.messaging import MessagingClient

@pytest.fixture
def messaging():
    customer_id = "FFFFFFFF-EEEE-DDDD-1234-AB1234567890"
    api_key = "ABC12345yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw=="
    return MessagingClient(customer_id, api_key, auth_method="Basic")

def test_omniMessage(messaging):
    phone_number = "11234567890"
    reference_id = "a" * 32
    
    params = {
        "recipient": {"phone_number": phone_number},
        "message": {
            "sms": {
                "parameters": {"text": "All purchases today are 20% off!"},
                "template": "text",
            }
        },
    }

    with patch.object(MessagingClient, 'post') as mock_post:
        mock_response = MagicMock(
            ok=True,
            json={
                "reference_id": reference_id,
                "status": {
                    "code": 3001,
                    "description": "Message in progress"
                }
            },
        )
        mock_post.return_value = mock_response

        response = messaging.omniMessage(params)

        mock_post.assert_called_once()
        called_url = mock_post.call_args[0][0]

        assert called_url == "/v1/omnichannel"
        assert response.ok
        assert response.json.get("reference_id") == reference_id
        assert response.json.get("status", {}).get("code") == 3001
        assert response.json.get("status", {}).get("description") == "Message in progress"