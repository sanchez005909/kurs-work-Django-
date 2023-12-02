from django.conf.urls.static import static
from django.urls import path
from django.conf import settings
from newsletter.apps import NewsletterConfig
from newsletter.views import ServiceClientCreateView, ServiceClientListView, ServiceClientUpdateView, index, \
    MailingListView, MailingCreateView, ServiceClientDeleteView, MailingDeleteView, MailingUpdateView

app_name = NewsletterConfig.name


urlpatterns = [
    path('', index, name='Главная'),
    path('list_clients', ServiceClientListView.as_view(), name='list_clients'),
    path('create_client', ServiceClientCreateView.as_view(), name='create_client'),
    path('update_client/<int:pk>/', ServiceClientUpdateView.as_view(), name='update_client'),
    path('delete_client/<int:pk>/', ServiceClientDeleteView.as_view(), name='delete_client'),
    path('list_mailings', MailingListView.as_view(), name='list_mailings'),
    path('create_mailing', MailingCreateView.as_view(), name='create_mailing'),
    path('update_mailing/<int:pk>/', MailingUpdateView.as_view(), name='update_mailing'),
    path('delete_mailing/<int:pk>/', MailingDeleteView.as_view(), name='delete_mailing'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)