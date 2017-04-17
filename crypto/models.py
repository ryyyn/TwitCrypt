from django.db import models

import datetime


class Auth(models.Model):
    hashed_code = models.CharField(max_length=128)
    hashed_pass = models.CharField(max_length=128)
    pass_salt = models.CharField(max_length=128)
    otp = models.CharField(max_length=1000)

    def exp_default(self):
        return datetime.datetime.now() + datetime.timedelta(days=1)

    exp_time = models.DateTimeField("expiration date", default=exp_default)

    def __str__(self):
        return self.hashed_code



# class decrypt(models.Model):
#     otp = models.CharField(max_length=1000)

