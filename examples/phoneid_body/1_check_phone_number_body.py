from __future__ import print_function
from telesignenterprise.phoneid import PhoneIdClient

def run():
    customer_id = "FFFFFFFF-EEEE-DDDD-1234-AB1234567890"
    api_key = "EXAMPLE----TE8sTgg45yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw=="
    phone_number = "phone_number"
    
    phoneid = PhoneIdClient(customer_id, api_key)
    response = phoneid.phone_id_body(phone_number)
    if response.ok:
        print("Response ",response.__dict__)