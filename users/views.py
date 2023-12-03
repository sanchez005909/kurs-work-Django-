from django.conf import settings
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.http import HttpRequest
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views import View
from django.views.generic import CreateView, UpdateView
from users.form import UserRegisterForm, UserForm
from users.models import User
from users.utils import generate_new_password


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        self.object = form.save()
        send_mail(
            subject='Регистрация нового пользователя',
            message=f'Для завершения регистрации перейдите по ссылке {self.get_verify_url(self.object)}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[self.object.email],
        )

        return super().form_valid(form)

    def get_verify_url(self, user):
        current_site = get_current_site(self.request)
        domain = current_site.domain
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = default_token_generator.make_token(user)
        url_path = reverse('users:verify_email', kwargs={'uidb64': uid, 'token': token})
        return f'http://{domain}{url_path}'


class EmailVerify(View):
    def get(self, request: HttpRequest, uidb64: str, token: str):
        user = self.get_user(uidb64)
        if not user or default_token_generator.check_token(user, token):
            messages.warning(self.request, 'Invalid reset link, please try to get it again')
        else:
            messages.success(self.request, 'Email successfully confirmed')
            user.is_active = True
            user.save()
        return redirect('users:login')

    def get_user(self, uid_base64: str) -> User | None:
        try:
            uid = urlsafe_base64_decode(uid_base64).decode()
            user_id = int(uid)
            user = User.objects.get(pk=user_id)
        except (ValueError, User.DoesNotExist):
            user = None
        return user


class ProfileView(LoginRequiredMixin, UpdateView):
    model = User
    success_url = reverse_lazy('users:profile')
    form_class = UserForm

    def get_object(self, queryset=None):
        return self.request.user






