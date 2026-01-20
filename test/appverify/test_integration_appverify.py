import pytest
import os
from telesignenterprise.appverify import AppVerifyClient

CUSTOMER_ID = os.getenv("CUSTOMER_ID", "FFFFFFFF-EEEE-DDDD-1234-AB1234567890")
API_KEY = os.getenv(
    "API_KEY",
    "ABC12345yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw==",
)


@pytest.fixture(scope="module")
def appverify():
    if not CUSTOMER_ID or not API_KEY:
        pytest.skip(
            "CUSTOMER_ID and API_KEY environment variables are required for integration tests."
        )
    return AppVerifyClient(CUSTOMER_ID, API_KEY)


def test_initiate_call(appverify):
    phone_number = "11234567890"

    initiate_response = appverify.initiate(phone_number)
    assert (
        initiate_response.ok
    ), f"Failed to initiate app verify call: {initiate_response.json}"
    reference_id = initiate_response.json.get("reference_id")
    assert reference_id, "Invalid reference_id returned"


def test_finalize_call(appverify):
    phone_number = "11234567890"

    initiate_response = appverify.initiate(phone_number)
    assert (
        initiate_response.ok
    ), f"Failed to initiate app verify call: {initiate_response.json}"
    reference_id = initiate_response.json.get("reference_id")
    assert reference_id, "Invalid reference_id returned"

    verify_code = "123456"

    finalize_response = appverify.finalize(reference_id, verify_code=verify_code)

    allowed_status_codes = (200, 400, 401, 404, 405, 429, 503)
    assert (
        finalize_response.ok or finalize_response.status_code in allowed_status_codes
    ), f"Unexpected finalize response: {finalize_response.json}"


def test_report_unknown_callerid(appverify):
    phone_number = "11234567890"

    initiate_response = appverify.initiate(phone_number)
    assert (
        initiate_response.ok
    ), f"Failed to initiate app verify call: {initiate_response.json}"
    reference_id = initiate_response.json.get("reference_id")
    prefix = initiate_response.json.get("prefix")
    assert reference_id and prefix, "Missing reference_id or prefix"

    unknown_caller_id = prefix + "99999"  # simulate unknownCallerId

    response = appverify.report_unknown_callerid(reference_id, unknown_caller_id)
    allowed_status_codes = (200, 400, 401, 404, 405, 429, 503)
    assert (
        response.ok or response.status_code in allowed_status_codes
    ), f"Unexpected report unknown caller ID response: {response.json}"


def test_report_timeout(appverify):
    phone_number = "11234567890"

    initiate_response = appverify.initiate(phone_number)
    assert (
        initiate_response.ok
    ), f"Failed to initiate app verify call: {initiate_response.json}"
    reference_id = initiate_response.json.get("reference_id")
    assert reference_id, "Missing reference_id"

    response = appverify.report_timeout(reference_id)
    allowed_status_codes = (200, 400, 401, 404, 405, 429, 503)
    assert (
        response.ok or response.status_code in allowed_status_codes
    ), f"Unexpected report timeout response: {response.json}"


def test_status(appverify):
    phone_number = "11234567890"

    initiate_response = appverify.initiate(phone_number)
    assert (
        initiate_response.ok
    ), f"Failed to initiate app verify call: {initiate_response.json}"
    reference_id = initiate_response.json.get("reference_id")
    assert reference_id, "Invalid reference_id returned"

    status_response = appverify.status(reference_id)
    assert status_response.ok, f"Failed to retrieve status: {status_response.json}"
    assert (
        "reference_id" in status_response.json
        and status_response.json["reference_id"] == reference_id
    )
