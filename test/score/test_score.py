import pytest
from unittest.mock import patch, MagicMock
from telesignenterprise.score import ScoreClient


@pytest.fixture
def score_client():
    customer_id = "FFFFFFFF-EEEE-DDDD-1234-AB1234567890"
    api_key = "ABC12345yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw=="
    return ScoreClient(customer_id, api_key)


def test_score_api_call(score_client):
    phone_number = "11234567890"
    account_lifecycle_event = "create"
    reference_id = "a" * 32

    with patch.object(ScoreClient, 'post') as mock_post:
        mock_response = MagicMock()
        mock_response.ok = True
        mock_response.json = {
            "reference_id": reference_id,
            "risk": {"level": "LOW", "recommendation": "allow"},
            "status": {"code": 300, "description": "Transaction successfully completed"}
        }
        mock_post.return_value = mock_response

        response = score_client.score(phone_number, account_lifecycle_event)

        mock_post.assert_called_once()
        called_url = mock_post.call_args[0][0]
        called_kwargs = mock_post.call_args[1]

        assert called_url == "/intelligence/phone"
        assert 'phone_number' in called_kwargs
        assert called_kwargs['phone_number'] == phone_number
        assert 'account_lifecycle_event' in called_kwargs
        assert called_kwargs['account_lifecycle_event'] == account_lifecycle_event

        assert response.ok
        assert response.json.get("reference_id") == reference_id


def test_score_with_optional(score_client):
    phone_number = "11234567890"
    event = "sign-in"
    account_id_val = "test_account"
    with patch.object(ScoreClient, 'post') as mock_post:
        mock_response = MagicMock()
        mock_response.ok = True
        mock_response.json = {
            "reference_id": "b" * 32,
            "risk": {"level": "LOW", "recommendation": "allow"},
            "status": {"code": 300, "description": "Transaction successfully completed"}
        }
        mock_post.return_value = mock_response

        response = score_client.score(phone_number, event, account_id=account_id_val)

        mock_post.assert_called_once()
        called_kwargs = mock_post.call_args[1]

        assert 'account_id' in called_kwargs
        assert called_kwargs['account_id'] == account_id_val

        assert response.ok
        assert response.json["risk"]["level"] == "LOW"