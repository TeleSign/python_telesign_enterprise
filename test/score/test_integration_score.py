import pytest
from telesignenterprise.score import ScoreClient
import os

CUSTOMER_ID = os.getenv("CUSTOMER_ID", "FFFFFFFF-EEEE-DDDD-1234-AB1234567890")
API_KEY = os.getenv(
    "API_KEY",
    "ABC12345yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw==",
)


@pytest.fixture(scope="module")
def score_client():
    return ScoreClient(CUSTOMER_ID, API_KEY)


def test_score_basic(score_client):
    phone_number = "11234567890"
    account_lifecycle_event = "create"
    response = score_client.score(phone_number, account_lifecycle_event)
    assert response.ok, f"Score failed: {response.json}"
    assert response.json.get("status", {}).get("code") in [
        300,
        301,
    ], f"Unexpected status: {response.json}"


def test_score_with_optional(score_client):
    phone_number = "11234567890"
    account_lifecycle_event = "sign-in"
    response = score_client.score(
        phone_number, account_lifecycle_event, account_id="test_account"
    )
    assert response.ok, f"Score with optional failed: {response.json}"
    assert response.json.get("status", {}).get("code") in [
        300,
        301,
    ], f"Unexpected status: {response.json}"
