import datetime

from django.test import TestCase
import encryption


class CryptoTests(TestCase):

    def encrypt_decrypt_py_test(self):
        # checks that the encryption and decryption python functions work
        otp = encryption.gen_otp()
        message = r"Test   dfg ABC 123450 ``` =+-_ &*!)@(*#&$% \t \n \\\\ \b \0 "
        code = encryption.encrypt(message, otp)
        decoded = encryption.decrypt(code, otp)
        self.assertIs(message == decoded, True)


CT = CryptoTests()
CT.encrypt_decrypt_py_test()