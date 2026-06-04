import pytest
from unittest.mock import patch, MagicMock
from telesignenterprise.telebureau import TelebureauClient

@pytest.fixture
def telebureau():
    customer_id = "FFFFFFFF-EEEE-DDDD-1234-AB1234567890"
    api_key = "ABC12345yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw=="
    return TelebureauClient(customer_id, api_key, auth_method="Basic")

def test_telebureau_create_event(telebureau):
    phone_number = "11234567890"
    reference_id = "a" * 32

    with patch.object(TelebureauClient, 'post') as mock_post:
        mock_response = MagicMock(
            ok=True,
            json={"reference_id": reference_id},
        )
        mock_post.return_value = mock_response

        response = telebureau.create_event(phone_number, "fraud_type_example", "2024-01-01T00:00:00Z")

        mock_post.assert_called_once()
        called_url = mock_post.call_args[0][0]

        assert called_url == "/v1/telebureau/event"
        assert response.ok
        assert response.json.get("reference_id") == reference_id

def test_telebureau_retrieve_event(telebureau):
    reference_id = "a" * 32

    with patch.object(TelebureauClient, 'get') as mock_get:
        mock_response = MagicMock(
            ok=True,
            json={"reference_id": reference_id},
        )
        mock_get.return_value = mock_response

        response = telebureau.retrieve_event(reference_id)

        mock_get.assert_called_once()
        called_url = mock_get.call_args[0][0]

        assert called_url == f"/v1/telebureau/event/{reference_id}"
        assert response.ok
        assert response.json.get("reference_id") == reference_id

def test_telebureau_delete_event(telebureau):
    reference_id = "a" * 32

    with patch.object(TelebureauClient, 'delete') as mock_delete:
        mock_response = MagicMock(
            ok=True,
            json={"reference_id": reference_id},
        )
        mock_delete.return_value = mock_response

        response = telebureau.delete_event(reference_id)

        mock_delete.assert_called_once()
        called_url = mock_delete.call_args[0][0]

        assert called_url == f"/v1/telebureau/event/{reference_id}"
        assert response.ok
        assert response.json.get("reference_id") == reference_id