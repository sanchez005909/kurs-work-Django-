from django.conf.urls.static import static
from django.urls import path
from django.conf import settings
from users.apps import UsersConfig
from users.views import UsersListView

app_name = UsersConfig.name

urlpatterns = [
    path('',  UsersListView.as_view(), name='Пользователи'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
