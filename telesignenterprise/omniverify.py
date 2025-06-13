from __future__ import unicode_literals

from telesign.rest import RestClient
from telesignenterprise.constants import SOURCE_SDK
import telesignenterprise
import telesign

BASE_URL_VERIFY_API = "https://verify.telesign.com"
PATH_VERIFICATION_CREATE = "/verification"
PATH_VERIFICATION_RETRIEVE = "/verification/{reference_id}"
PATH_VERIFICATION_UPDATE = "/verification/{reference_id}/state"

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

    def createVerificationProcess(self, phone_number, params={}):
        """
        Create a verification process for the specified phone number.

        See https://developer.telesign.com/enterprise/reference/createverificationprocess for detailed API documentation.
        """
        params["recipient"] = {"phone_number": phone_number}

        if "verification_policy" not in params:
            params["verification_policy"] = [{"method": "sms"}]

        return self.post(PATH_VERIFICATION_CREATE, json_fields=params)    

    def getVerificationProcess(self, reference_id, params={}):
        """
        Retrieve details about the specified verification process.

        See https://developer.telesign.com/enterprise/reference/getverificationprocess or detailed API documentation.
        
        :param reference_id: The unique identifier of the verification process.
        :param params: Optional query parameters as a dictionary.
        :return: Response object from the GET request.
        """
        endpoint = PATH_VERIFICATION_RETRIEVE.format(reference_id=reference_id)
        headers = {"Content-Type": "application/json", "Accept": "application/json"}

        return self.get(endpoint, json_fields=params, headers=headers)    
    
    def updateVerificationProcess(self, reference_id, params):
        """
        Update a verification process

        See https://developer.telesign.com/enterprise/reference/updateverificationprocess for detailed API documentation.

        :param reference_id: The unique identifier of the verification process.
        :param params: Dictionary of parameters for the update (must include 'action' and 'security_factor').
        :return: Response object from the PATCH request.
        """
        endpoint = PATH_VERIFICATION_UPDATE.format(reference_id=reference_id)
        headers = {"Content-Type": "application/json", "Accept": "application/json"}
        return self.patch(endpoint, json_fields=params, headers=headers) 