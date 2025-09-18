import pytest
from unittest.mock import patch, MagicMock
from telesignenterprise.appverify import AppVerifyClient


@pytest.fixture
def appverify():
    customer_id = "FFFFFFFF-EEEE-DDDD-1234-AB1234567890"
    api_key = "ABC12345yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw=="
    return AppVerifyClient(customer_id, api_key)


def test_initiate_call(appverify):
    with patch.object(AppVerifyClient, "post") as mock_post:
        mock_response = MagicMock()
        mock_response.ok = True
        mock_response.json = {"test": "response"}
        mock_post.return_value = mock_response

        phone_number = "11234567890"
        response = appverify.initiate(phone_number)

        mock_post.assert_called_once()
        called_url = mock_post.call_args[0][0]
        called_params = mock_post.call_args[1]

        assert called_url == "/v1/verify/auto/voice/initiate"
        assert called_params["phone_number"] == phone_number
        assert response.ok is True
        assert isinstance(response.json, dict)


def test_finalize_call(appverify):
    with patch.object(AppVerifyClient, "post") as mock_post:
        mock_response = MagicMock()
        mock_response.ok = True
        mock_response.json = {"test": "response"}
        mock_post.return_value = mock_response

        reference_id = "test_reference_id"
        response = appverify.finalize(reference_id)

        mock_post.assert_called_once()
        called_url = mock_post.call_args[0][0]
        called_params = mock_post.call_args[1]

        assert called_url == "/v1/verify/auto/voice/finalize"
        assert called_params["reference_id"] == reference_id
        assert response.ok is True
        assert isinstance(response.json, dict)


def test_report_unknown_callerid(appverify):
    with patch.object(AppVerifyClient, "post") as mock_post:
        mock_response = MagicMock()
        mock_response.ok = True
        mock_response.json = {"test": "response"}
        mock_post.return_value = mock_response

        reference_id = "test_reference_id"
        unknown_caller_id = "1234567890"
        response = appverify.report_unknown_callerid(reference_id, unknown_caller_id)

        mock_post.assert_called_once()
        called_url = mock_post.call_args[0][0]
        called_params = mock_post.call_args[1]

        assert called_url == "/v1/verify/auto/voice/finalize/callerid"
        assert called_params["reference_id"] == reference_id
        assert called_params["unknown_caller_id"] == unknown_caller_id
        assert response.ok is True
        assert isinstance(response.json, dict)


def test_report_timeout(appverify):
    with patch.object(AppVerifyClient, "post") as mock_post:
        mock_response = MagicMock()
        mock_response.ok = True
        mock_response.json = {"test": "response"}
        mock_post.return_value = mock_response

        reference_id = "test_reference_id"
        response = appverify.report_timeout(reference_id)

        mock_post.assert_called_once()
        called_url = mock_post.call_args[0][0]
        called_params = mock_post.call_args[1]

        assert called_url == "/v1/verify/auto/voice/finalize/timeout"
        assert called_params["reference_id"] == reference_id
        assert response.ok is True
        assert isinstance(response.json, dict)


def test_status(appverify):
    with patch.object(AppVerifyClient, "get") as mock_get:
        mock_response = MagicMock()
        mock_response.ok = True
        mock_response.json = {"test": "response"}
        mock_get.return_value = mock_response

        reference_id = "test_reference_id"
        response = appverify.status(reference_id)

        mock_get.assert_called_once()
        called_url = mock_get.call_args[0][0]

        expected_url = f"/v1/verify/auto/voice/{reference_id}"
        assert called_url == expected_url
        assert response.ok is True
        assert isinstance(response.json, dict)