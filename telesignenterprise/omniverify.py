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
        super(OmniVerify, self).__init__(
            customer_id,
            api_key,
            rest_endpoint=rest_endpoint,
            **kwargs
        )
        self.rest_endpoint = rest_endpoint

    def createVerificationProcess(self, phone_number, params={}):
        """
        Use this action to create a verification process for the specified phone number.

        See https://developer.telesign.com/enterprise/reference/createverificationprocess for detailed API documentation.
        """
        params["recipient"] = {"phone_number": phone_number}

        if "verification_policy" not in params:
            params["verification_policy"] = [{"method": "sms"}]

        self.set_endpoint(BASE_URL_VERIFY_API)
        return self.post(PATH_VERIFICATION_CREATE, json_fields=params)    

    def getVerificationProcess(self, reference_id, params={}):
        """
        Retrieve details about the specified verification process.

        :param reference_id: The unique identifier of the verification process.
        :param params: Optional query parameters as a dictionary.
        :return: Response object from the GET request.
        """
        assert isinstance(reference_id, str) and len(reference_id) == 32, "reference_id must be a 32-character string"

        endpoint = PATH_VERIFICATION_RETRIEVE.format(reference_id=reference_id)
        self.set_endpoint(self.rest_endpoint)
        headers = {"Content-Type": "application/json", "Accept": "application/json"}

        return self.get(endpoint, params=params, headers=headers)    