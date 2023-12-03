from django.conf.urls.static import static
from django.urls import path
from django.conf import settings
from newsletter.apps import NewsletterConfig
from newsletter.views import (ServiceClientCreateView, ServiceClientListView, ServiceClientUpdateView,
                              MailingListView, MailingCreateView, ServiceClientDeleteView, MailingDeleteView,
                              MailingUpdateView, MailingLogListView, toggle_active_client, toggle_active_mailing,
                              MyTemplateView)

app_name = NewsletterConfig.name

urlpatterns = [
                  path('', MyTemplateView.as_view(), name='Главная'),
                  path('list_clients', ServiceClientListView.as_view(), name='list_clients'),
                  path('create_client', ServiceClientCreateView.as_view(), name='create_client'),
                  path('update_client/<int:pk>/', ServiceClientUpdateView.as_view(), name='update_client'),
                  path('delete_client/<int:pk>/', ServiceClientDeleteView.as_view(), name='delete_client'),
                  path('list_mailings', MailingListView.as_view(), name='list_mailings'),
                  path('create_mailing', MailingCreateView.as_view(), name='create_mailing'),
                  path('update_mailing/<int:pk>/', MailingUpdateView.as_view(), name='update_mailing'),
                  path('delete_mailing/<int:pk>/', MailingDeleteView.as_view(), name='delete_mailing'),
                  path('report_list', MailingLogListView.as_view(), name='report_list'),
                  path('mailing_set_active/<int:pk>', toggle_active_mailing, name='set_active'),
                  path('set_active_client/<int:pk>', toggle_active_client, name='set_active_client')
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
