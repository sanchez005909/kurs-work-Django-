from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth.decorators import permission_required
from newsletter.models import ServiceClient, Mailing, MailingLog
from newsletter.forms import ServiceClientForm, MailingForm
from newsletter.utils import change_active_object


def index(request):
    return render(request, 'newsletter/main_page.html')


class ServiceClientListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = ServiceClient
    permission_required = 'newsletter.view_client'
    template_name = 'newsletter/list_client.html'

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        if self.request.user.is_staff or self.request.user.is_superuser:
            queryset = queryset.all()
        else:
            queryset = queryset.filter(owner=self.request.user)
        return queryset


class ServiceClientCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = ServiceClient
    form_class = ServiceClientForm
    permission_required = 'newsletter.create_client'
    template_name = 'newsletter/form_client.html'
    success_url = reverse_lazy('newsletter:list_clients')


@permission_required('newsletter.set_active_client')
def toggle_active_client(request, pk):
    change_active_object(request, ServiceClient, pk)
    return redirect(reverse('newsletter:list_clients'))


class ServiceClientUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = ServiceClient
    form_class = ServiceClientForm
    permission_required = 'newsletter.change_client'
    template_name = 'newsletter/form_client.html'
    success_url = reverse_lazy('newsletter:list_clients')


class ServiceClientDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = ServiceClient
    permission_required = 'newsletter.delete_client'
    template_name = 'newsletter/delete.html'
    success_url = reverse_lazy('newsletter:list_clients')


class MailingCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Mailing
    form_class = MailingForm
    permission_required = 'newsletter.create_mailing'
    template_name = 'newsletter/form_mailing.html'
    success_url = reverse_lazy('newsletter:list_mailings')


class MailingListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Mailing
    permission_required = 'newsletter.view_mailing'
    template_name = 'newsletter/list_mailings.html'


@permission_required('newsletter.set_active')
def toggle_active_mailing(request, pk):
    change_active_object(request, Mailing, pk)
    return redirect(reverse('newsletter:list_mailings'))


class MailingUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Mailing
    form_class = MailingForm
    permission_required = 'newsletter.change_mailing'
    template_name = 'newsletter/form_mailing.html'
    success_url = reverse_lazy('newsletter:list_mailings')


class MailingDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Mailing
    permission_required = 'newsletter.delete_mailing'
    template_name = 'newsletter/delete.html'
    success_url = reverse_lazy('newsletter:list_mailings')


class MailingLogListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = MailingLog
    permission_required = 'newsletter.view_mailinglog'
    template_name = 'newsletter/report_list_mailings.html'
