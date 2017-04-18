import datetime

from django.test import TestCase
import encryption
# from .models import *


class CryptoTests(TestCase):

    def encrypt_decrypt_py_test(self):
        # checks that the encryption and decryption python functions work
        otp = encryption.gen_otp()
        message = r"Test Message     abcdefg ABCDEFG 1234500 ~` =+-_ &*!)@(*#&$% \t \n \\\\ \b \0 "
        code = encryption.encrypt(message, otp)
        decoded = encryption.decrypt(code, otp)
        self.assertIs(message == decoded, True)

    def otp_unique(self):
        # tests otp generation for uniqueness
        otp_arr = [encryption.gen_otp() * 10000]
        self.assertIs(len(set(otp_arr)) == len(otp_arr), True )

