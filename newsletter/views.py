from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from newsletter.models import ServiceClient, Mailing
from newsletter.forms import ServiceClientForm, MailingForm


def index(request):
    return render(request, 'newsletter/main_page.html')


class ServiceClientListView(ListView):
    model = ServiceClient
    template_name = 'newsletter/list_client.html'


class ServiceClientCreateView(CreateView):
    model = ServiceClient
    form_class = ServiceClientForm
    template_name = 'newsletter/form_client.html'
    success_url = reverse_lazy('newsletter:list_clients')


class ServiceClientUpdateView(UpdateView):
    model = ServiceClient
    form_class = ServiceClientForm
    template_name = 'newsletter/form_client.html'
    success_url = reverse_lazy('newsletter:list_clients')


class ServiceClientDeleteView(DeleteView):
    model = ServiceClient
    template_name = 'newsletter/delete.html'
    success_url = reverse_lazy('newsletter:list_clients')


class MailingCreateView(CreateView):
    model = Mailing
    form_class = MailingForm
    template_name = 'newsletter/form_mailing.html'
    success_url = reverse_lazy('newsletter:list_mailings')


class MailingListView(ListView):
    model = Mailing
    template_name = 'newsletter/list_mailings.html'


class MailingUpdateView(UpdateView):
    model = Mailing
    form_class = MailingForm
    template_name = 'newsletter/form_mailing.html'
    success_url = reverse_lazy('newsletter:list_mailings')


class MailingDeleteView(DeleteView):
    model = Mailing
    template_name = 'newsletter/delete.html'
    success_url = reverse_lazy('newsletter:list_mailings')
