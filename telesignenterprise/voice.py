from __future__ import unicode_literals

from telesign.voice import VoiceClient as _VoiceClient
from telesignenterprise.constants import SOURCE_SDK
import telesignenterprise
import telesign


class VoiceClient(_VoiceClient):
    """
    TeleSign's Voice API allows you to easily send voice messages. You can send alerts, reminders, and notifications,
    or you can send verification messages containing time-based, one-time passcodes (TOTP).
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
        super(VoiceClient, self).__init__(
            customer_id,
            api_key,
            rest_endpoint=rest_endpoint,
            source=SOURCE_SDK,
            sdk_version_origin=sdk_version_origin,
            sdk_version_dependency=sdk_version_dependency,
            **kwargs
        )
