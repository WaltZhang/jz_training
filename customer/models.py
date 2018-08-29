from django.db import models
from django.utils.translation import ugettext


class IdentityRegistry(models.Model):
    name = models.CharField(max_length=20)
    gender = models.CharField(max_length=2)
    identity = models.CharField(max_length=18)
    birthday = models.CharField(max_length=14)
    authorization_office = models.CharField(max_length=30)
    address = models.CharField(max_length=40)
    validity_period = models.CharField(max_length=20)
    id_card_url = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=12)

    def __str__(self):
        return self.name + ' : ' + self.phone_number


class Loan(models.Model):
    use = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    amount = models.IntegerField()
    identity = models.CharField(max_length=18)
    education = models.IntegerField()
