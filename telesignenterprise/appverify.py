from __future__ import unicode_literals

from telesign.rest import RestClient
from telesignenterprise.constants import SOURCE_SDK
import telesignenterprise
import telesign

APP_VERIFY_BASE_RESOURCE = "/v1/verify/auto/voice"
APP_VERIFY_INITIATE_RESOURCE = APP_VERIFY_BASE_RESOURCE + "/initiate"
APP_VERIFY_FINALIZE_RESOURCE = APP_VERIFY_BASE_RESOURCE + "/finalize"
APP_VERIFY_FINALIZE_CALLERID_RESOURCE = APP_VERIFY_BASE_RESOURCE + "/finalize/callerid"
APP_VERIFY_FINALIZE_TIMEOUT_RESOURCE = APP_VERIFY_BASE_RESOURCE + "/finalize/timeout"
APP_VERIFY_STATUS_RESOURCE = APP_VERIFY_BASE_RESOURCE + "/{}"


class AppVerifyClient(RestClient):
    """
    The TeleSign App Verify web service enables customers to verify devices
    through a voice call by a verification code provided in the caller ID.
    """

    def __init__(
        self,
        customer_id,
        api_key,
        rest_endpoint="https://rest-ww.telesign.com",
        **kwargs
    ):
        sdk_version_origin = telesignenterprise.__version__
        sdk_version_dependency = telesign.__version__
        super(AppVerifyClient, self).__init__(
            customer_id,
            api_key,
            rest_endpoint=rest_endpoint,
            source=SOURCE_SDK,
            sdk_version_origin=sdk_version_origin,
            sdk_version_dependency=sdk_version_dependency,
            **kwargs
        )

    def initiate(self, phone_number, **params):
        """
        Use this endpont to initiate verification of the specified phone number using the Telesign App Verify API.

        :param phone_number: The phone number to verify
        :param params: Additional optional parameters
        :return: API response object

        See https://developer.telesign.com/enterprise/reference/sendappverifycode for detailed API documentation.
        """
        return self.post(
            APP_VERIFY_INITIATE_RESOURCE, phone_number=phone_number, **params
        )

    def finalize(self, reference_id, **params):
        """
        Use this endpoint to terminate a call created using the Telesign App Verify API 
        if the handset does not terminate the call in your application.

        :param reference_id: The reference ID of the verification transaction
        :param params: Additional optional parameters
        :return: API response object

        See https://developer.telesign.com/enterprise/reference/endappverifycall for detailed API documentation.
        """
        return self.post(
            APP_VERIFY_FINALIZE_RESOURCE, reference_id=reference_id, **params
        )

    def status(self, reference_id, **params):
        """
        Use this endpoint to get the status of a Telesign App Verify API request that you initiated.
        
        :param reference_id: The reference ID of the verification transaction
        :param params: Additional optional parameters
        :return: API response object

        See https://developer.telesign.com/enterprise/reference/getappverifystatus for detailed API documentation.
        """
        return self.get(APP_VERIFY_STATUS_RESOURCE.format(reference_id), **params)
    
    def report_unknown_callerid(self, reference_id, unknown_caller_id):
        """
        If a Telesign App Verify API call is unsuccessful, the device will not receive the call. 
        If there is a prefix sent by Telesign in the initiate request and it cannot be matched to the CLI of the verification call, 
        you can use use this endpoint to report the issue to Telesign for troubleshooting.

        :param reference_id: The reference ID of the verification transaction
        :param unknown_caller_id: The unknown caller ID to report
        :return: API response object

        See https://developer.telesign.com/enterprise/reference/reportappverifycallerid for detailed API documentation.
        """
        params = {
            "reference_id": reference_id,
            "unknown_caller_id": unknown_caller_id,
        }
        return self.post(APP_VERIFY_FINALIZE_CALLERID_RESOURCE, **params)

    def report_timeout(self, reference_id):
        """
        Use this endpont to initiate verification of the specified phone number using the Telesign App Verify API.

        :param reference_id: The reference ID of the verification transaction
        :return: API response object

        See https://developer.telesign.com/enterprise/reference/reportappverifytimeout for detailed API documentation.
        """
        params = {
            "reference_id": reference_id,
        }
        return self.post(APP_VERIFY_FINALIZE_TIMEOUT_RESOURCE, **params)