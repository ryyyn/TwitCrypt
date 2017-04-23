from django.db import models

import datetime


class CodeRecord(models.Model):
    code = models.CharField(
        verbose_name="Text",
        max_length=140,
    )
    password = models.CharField(max_length=100)
    otp = models.CharField(max_length=1000)
    exp_time = models.DateTimeField("Expiration date",
                                    default=datetime.datetime.now() + datetime.timedelta(days=1))

    def __str__(self):
        return self.code

