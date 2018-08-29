from django.views.generic.base import TemplateView
from django.views.generic import FormView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy, reverse

from .forms import CustomerForm, CreateIdentityForm, CreateApplyForm
from .models import IdentityRegistry


class CreateCustomerView(FormView):
    form_class = CustomerForm
    template_name = 'customer/register.html'

    def get_success_url(self):
        return reverse('customer:identity') + '?phone_number=' + self.phone_number

    def form_valid(self, form):
        self.phone_number = self.request.POST['phone_number']
        return super().form_valid(form)


class IdentityView(CreateView):
    form_class = CreateIdentityForm
    template_name = 'customer/identity.html'

    def get_success_url(self):
        return reverse('customer:apply') + '?customer_pk=' + self.customer_pk

    def form_valid(self, form):
        id_reg = IdentityRegistry.objects.first()
        if id_reg is not None:
            id_reg.phone_number = self.request.GET.get('phone_number')
            id_reg.save()
            self.customer_pk = id_reg.pk
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['phone_number'] = self.request.GET.get('phone_number')
        # TODO: Only one Identity model, currently.
        id_reg = IdentityRegistry.objects.first()
        if id_reg is not None:
            context['name'] = id_reg.name
            context['gender'] = id_reg.gender
            context['identity'] = id_reg.identity
            context['birthday'] = id_reg.birthday
            context['authorization_office'] = id_reg.authorization_office
            context['address'] = id_reg.address
            context['validity_period'] = id_reg.validity_period
            context['id_card_url'] = id_reg.id_card_url
        return context


class CreateApplyView(CreateView):
    form_class = CreateApplyForm
    template_name = 'customer/apply.html'
    success_url = reverse_lazy('customer:result')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['phone_number'] = self.request.GET.get('phone_number')
        return context
