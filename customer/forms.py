from django.utils.translation import ugettext
from django.contrib.auth.forms import forms

from .models import IdentityRegistry, Loan

HOUSING_LOAN = 'housing_loan'
WARRANTY_LOAN = 'warranty_loan'
PRODUCT_TYPES = [
    (WARRANTY_LOAN, ugettext('保单贷')),
    (HOUSING_LOAN, ugettext('房供贷')),
]

class CustomerForm(forms.Form):
        product = forms.ChoiceField(label=ugettext('产品'), choices=PRODUCT_TYPES, widget=forms.Select(attrs={
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
            fields = [
                'product',
                'salesman',
                'customer_source',
                'phone_number',
                'verified_code',
            ]


class CreateIdentityForm(forms.ModelForm):
    name = forms.CharField(label=ugettext('姓名'), widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    gender = forms.CharField(label=ugettext('性别'), widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    identity = forms.CharField(label=ugettext('身份证号码'), widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    birthday = forms.CharField(label=ugettext('出生日期'), widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    authorization_office = forms.CharField(label=ugettext('签发机关'), widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    address = forms.CharField(label=ugettext('地址'), widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    validity_period = forms.CharField(label=ugettext('有效期限'), widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    id_card_url = forms.CharField(label=ugettext('身份证图片'), widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))

    class Meta:
        model = IdentityRegistry
        fields = [
            'name',
            'gender',
            'identity',
            'birthday',
            'authorization_office',
            'address',
            'validity_period',
            # 'id_card_url',
        ]


LOAN_USES = [
    ('personal_consumption', ugettext('个人消费')),
]
LOAN_AMOUNTS = [
    ('l1', ugettext('20-30万')),
    ('l2', ugettext('30-50万')),
    ('l3', ugettext('50万以上')),
]
EDUCATION_LEVEL = [
    ('1', ugettext('小学以下')),
    ('2', ugettext('初中')),
    ('3', ugettext('中专或高中')),
    ('4', ugettext('专科')),
    ('5', ugettext('本科')),
    ('6', ugettext('研究生及以上')),
]

class CreateApplyForm(forms.ModelForm):
    use = forms.ChoiceField(label=ugettext('贷款用途及贷款用途子类'), choices=LOAN_USES, widget=forms.Select(attrs={
        'class': 'form-control',
    }))
    description = forms.CharField(label=ugettext(''), widget=forms.Textarea(attrs={
        'class': 'form-control',
        'rows': 5,
    }))
    amount = forms.ChoiceField(label=ugettext('申请金额'), choices=LOAN_AMOUNTS, widget=forms.Select(attrs={
        'class': 'form-control',
    }))
    education = forms.ChoiceField(label=ugettext('教育程度'), choices=EDUCATION_LEVEL, widget=forms.RadioSelect(attrs={
        'class': 'col-3',
    }))

    class Meta:
        model = Loan
        fields = [
            'use',
            'description',
            'amount',
            # 'education',
        ]
