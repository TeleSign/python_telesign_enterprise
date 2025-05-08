from __future__ import unicode_literals

from telesign.score import ScoreClient as _ScoreClient
from telesignenterprise.constants import SOURCE_SDK
import telesignenterprise
import telesign


class ScoreClient(_ScoreClient):
    """
    Score provides risk information about a specified phone number.
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
        super(ScoreClient, self).__init__(
            customer_id,
            api_key,
            rest_endpoint=rest_endpoint,
            source=SOURCE_SDK,
            sdk_version_origin=sdk_version_origin,
            sdk_version_dependency=sdk_version_dependency,
            **kwargs
        )
