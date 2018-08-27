from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy, reverse

from .forms import CreateCustomerForm


class CreateCustomerView(CreateView):
    form_class = CreateCustomerForm
    template_name = 'customer/register.html'

    def get_success_url(self):
        return reverse('customer:identity') + '?phone=' + self.phone

    def form_valid(self, form):
        self.phone = self.request.GET['phone_number']
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)

class IdentityView(TemplateView):
    template_name = 'customer/identity.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['phone'] = self.request.GET['phone']
        return context
