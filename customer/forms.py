from django.utils.translation import ugettext
from django.contrib.auth.forms import forms

from .models import CustomerRegister


class CreateCustomerForm(forms.ModelForm):
        product = forms.ChoiceField(label=ugettext('产品'), choices=CustomerRegister.PRODUCT_TYPES, widget=forms.Select(attrs={
            'class': 'form-control',
        }))
        salesman = forms.CharField(label=ugettext('销售人员'), widget=forms.TextInput(attrs={
            'class': 'form-control',
        }))
        customer_source = forms.CharField(label=ugettext('客户来源'), widget=forms.TextInput(attrs={
            'class': 'form-control',
        }))
        phone_number = forms.CharField(label=ugettext('客户手机号'), widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': ugettext('请填写客户手机号'),
            'id': 'phone_number',
            'name': 'phone_number',
        }))
        verified_code = forms.CharField(label=ugettext('验证码'), widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': ugettext('请填写验证码'),
        }))

        class Meta:
            model = CustomerRegister
            fields = [
                'product',
                'salesman',
                'customer_source',
                'phone_number',
                'verified_code',
            ]
