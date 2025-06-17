from __future__ import unicode_literals

from telesign.rest import RestClient
from telesignenterprise.constants import SOURCE_SDK
import telesignenterprise
import telesign
import requests, json, base64

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

        See https://developer.telesign.com/enterprise/reference/getverificationprocess for detailed API documentation.
        
        :param reference_id: The unique identifier of the verification process.
        :param params: Optional query parameters as a dictionary.
        :return: Response object from the GET request.
        """
        endpoint = PATH_VERIFICATION_RETRIEVE.format(reference_id=reference_id)
        headers = {"Content-Type": "application/json", "Accept": "application/json"}

        return self.get(endpoint, json_fields=params, headers=headers)    
    
    def updateVerificationProcess(self, reference_id, params, use_basic_auth=False):
        """
        Update a verification process.

        See https://developer.telesign.com/enterprise/reference/updateverificationprocess for detailed API documentation.

        :param reference_id: The unique identifier of the verification process.
        :param params: Dictionary of parameters for the update (must include 'action' and 'security_factor').
        :param use_basic_auth: Boolean indicating whether to use manual Basic Auth.
        :return: Response object.
        """
        endpoint_path = PATH_VERIFICATION_UPDATE.format(reference_id=reference_id)

        if use_basic_auth:
            endpoint = self.api_host.rstrip('/') + endpoint_path

            json_body = json.dumps(params)

            auth_str = f"{self.customer_id}:{self.api_key}"
            auth_bytes = auth_str.encode('utf-8')
            auth_b64 = base64.b64encode(auth_bytes).decode('utf-8')
            headers = {
                "Authorization": f"Basic {auth_b64}",
                "Content-Type": "application/json",
                "Accept": "application/json"
            }
            response = requests.patch(endpoint, data=json_body, headers=headers)
            return type('Response', (), {
                'status_code': response.status_code,
                'headers': response.headers,
                'body': response.text,
                'ok': response.ok,
                'json': response.json
            })()
        else:
            headers = {"Content-Type": "application/json", "Accept": "application/json"}
            return self.patch(endpoint_path, json_fields=params, headers=headers)