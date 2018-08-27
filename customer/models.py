from django.db import models
from django.utils.translation import ugettext


class CustomerRegister(models.Model):
    HOUSING_LOAN = 'housing_loan'
    WARRANTY_LOAN = 'warranty_loan'
    PRODUCT_TYPES = [
        (HOUSING_LOAN, ugettext('房供贷')),
        (WARRANTY_LOAN, ugettext('保单贷')),
    ]


class IdentityRegister(models.Model):
    name = models.CharField(max_length=20)
    gender = models.CharField(max_length=2)
    identity = models.CharField(max_length=18)
    birthday = models.CharField(max_length=14)
    authorization_office = models.CharField(max_length=30)
    address = models.CharField(max_length=40)
    validity_period = models.CharField(max_length=20)
    id_card_url = models.CharField(max_length=250)
