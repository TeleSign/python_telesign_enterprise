from __future__ import unicode_literals

from telesign.rest import RestClient
from telesignenterprise.constants import SOURCE_SDK
import telesignenterprise
import telesign

BASE_URL_VERIFY_API = "https://verify.telesign.com"
PATH_VERIFICATION_CREATE = "/verification"
PATH_VERIFICATION_RETRIEVE = "/verification/{reference_id}"

class OmniVerify(RestClient):
    """
    OmniVerify class to handle omnichannel verification API calls.
    """

    def __init__(self, customer_id, api_key, rest_endpoint=BASE_URL_VERIFY_API, **kwargs):
        """
        Initializes the OmniVerify client with SDK versioning for traceability.
        """
        sdk_version_origin = telesignenterprise.__version__
        sdk_version_dependency = telesign.__version__

        super(OmniVerify, self).__init__(
            customer_id,
            api_key,
            rest_endpoint=rest_endpoint,
            source=SOURCE_SDK,
            sdk_version_origin=sdk_version_origin,
            sdk_version_dependency=sdk_version_dependency,
            **kwargs
        )

    def createVerificationProcess(self, phone_number, params=None):
        """
        Create a verification process for the specified phone number.

        See https://developer.telesign.com/enterprise/reference/createverificationprocess for detailed API documentation.
        """
        params["recipient"] = {"phone_number": phone_number}

        if "verification_policy" not in params:
            params["verification_policy"] = [{"method": "sms"}]

        return self.post(PATH_VERIFICATION_CREATE, json_fields=params)    

    def getVerificationProcess(self, reference_id, params=None):
        """
        Retrieve details about the specified verification process.

        :param reference_id: The unique identifier of the verification process.
        :param params: Optional query parameters as a dictionary.
        :return: Response object from the GET request.
        """
        if params is None:
            params = {}
        endpoint = PATH_VERIFICATION_RETRIEVE.format(reference_id=reference_id)
        headers = {"Content-Type": "application/json", "Accept": "application/json"}

        return self.get(endpoint, json_fields=params, headers=headers)    