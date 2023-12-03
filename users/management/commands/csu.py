from users.models import User

from django.core.management import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin@tol.as',
            first_name='Admin',
            last_name='TolAS',
            is_active=True,
            is_staff=True,
            is_superuser=True,
        )

        user.set_password("12345")
        user.save()
