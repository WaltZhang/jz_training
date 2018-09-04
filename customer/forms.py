from django.utils.translation import ugettext
from django.contrib.auth.forms import forms

from .models import IdentityRegistry, Loan

HOUSING_LOAN = 'housing_loan'
WARRANTY_LOAN = 'warranty_loan'
PRODUCT_TYPES = [
    (HOUSING_LOAN, ugettext('房供贷')),
    (WARRANTY_LOAN, ugettext('保单贷')),
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
    ('1', ugettext('经营用途')),
    ('2', ugettext('个人消费')),
    ('3', ugettext('农牧业用途')),
]
LOAN_AMOUNTS = [
    ('1', ugettext('10万以下')),
    ('2', ugettext('10-20万')),
    ('3', ugettext('20-30万')),
]
EDUCATION_LEVEL = [
    ('1', ugettext('小学以下')),
    ('2', ugettext('初中')),
    ('3', ugettext('中专或高中')),
    ('4', ugettext('专科')),
    ('5', ugettext('本科')),
    ('6', ugettext('研究生及以上')),
]
MARRIAGE_STATE = [
    ('1', ugettext('未婚')),
    ('2', ugettext('已婚')),
    ('3', ugettext('其他')),
]
MEMBER_OF_FAMILY = [
    ('1', ugettext('一人及以下')),
    ('2', ugettext('二人')),
    ('3', ugettext('三人')),
    ('4', ugettext('四人及以上')),
]
INCOMING_LEVEL = [
    ('1', ugettext('2000及以下')),
    ('2', ugettext('2001 - 5000')),
    ('3', ugettext('5001 - 10000')),
    ('4', ugettext('10001 - 20000')),
    ('5', ugettext('20001 - 50000')),
    ('6', ugettext('50001及以上')),
]
PROPERTIES = [
    ('1', ugettext('与父母同住')),
    ('2', ugettext('租用房屋')),
    ('3', ugettext('本人房产（无按揭）')),
    ('4', ugettext('本人房产（有按揭）')),
    ('5', ugettext('集体宿舍（无房租）')),
    ('6', ugettext('朋友、亲戚家及其他')),
]
VEHICLES = [
    ('1', ugettext('步行、自行车')),
    ('2', ugettext('摩托、电瓶车')),
    ('3', ugettext('公共交通')),
    ('4', ugettext('自驾汽车')),
    ('5', ugettext('其他')),
]
EMPLOYMENTS = [
    ('1', ugettext('国有企业')),
    ('2', ugettext('政府或非营利机构')),
    ('3', ugettext('私营、外企')),
    ('4', ugettext('小企业主或个体经营者')),
    ('5', ugettext('农民')),
    ('6', ugettext('无固定工作、自由职业')),
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
    education = forms.ChoiceField(label=ugettext('教育程度'), choices=EDUCATION_LEVEL, widget=forms.RadioSelect())
    marriage = forms.ChoiceField(label=ugettext('婚姻状况'), choices=MARRIAGE_STATE, widget=forms.RadioSelect())
    members = forms.ChoiceField(label=ugettext('家庭人口'), choices=MEMBER_OF_FAMILY, widget=forms.RadioSelect())
    incoming = forms.ChoiceField(label=ugettext('收入水平（全年收入月平均）'), choices=INCOMING_LEVEL, widget=forms.RadioSelect())
    property = forms.ChoiceField(label=ugettext('居住类型'), choices=PROPERTIES, widget=forms.RadioSelect())
    vehicle = forms.ChoiceField(label=ugettext('主要出行交通工具'), choices=VEHICLES, widget=forms.RadioSelect())
    residence = forms.CharField(label=ugettext('住宅地址'), widget=forms.HiddenInput())
    employment = forms.ChoiceField(label=ugettext('受雇类型'), choices=EMPLOYMENTS, widget=forms.RadioSelect())
    company = forms.CharField(label=ugettext('公司名称'), required=False, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'style': 'display:none',
    }))

    class Meta:
        model = Loan
        fields = [
        ]
