from __future__ import print_function
from telesignenterprise.verify import VerifyClient
from telesign.util import random_with_n_digits

customer_id = "FFFFFFFF-EEEE-DDDD-1234-AB1234567890"
api_key = "EXAMPLE----TE8sTgg45yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw=="

phone_number = "phone_number"
verify_code = random_with_n_digits(5)
tts_message = "Hello, your code is {verify_code}. Once again, your code is {verify_code}. Goodbye.".format(
    verify_code=", ".join(list(verify_code)))

verify = VerifyClient(customer_id, api_key)
response = verify.voice(phone_number, tts_message=tts_message)

user_entered_verify_code = raw_input("Please enter the verification code you were sent: ")

if verify_code == user_entered_verify_code.strip():
    print("Your code is correct.")
else:
    print("Your code is incorrect.")
