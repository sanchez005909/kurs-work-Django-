from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from users.models import Users


# Create your views here.
class UsersListView(ListView):
    model = Users
    template_name = reverse_lazy('users:list_users.html')


class UsersCreateView(CreateView):
    model = Users
    template_name = reverse_lazy('users:form_users.html')


class UsersUpdateView(UpdateView):
    model = Users
    template_name = reverse_lazy('users:form_users.html')


class UsersDeleteView(DeleteView):
    model = Users
    template_name = reverse_lazy('users:delete_user.html')
