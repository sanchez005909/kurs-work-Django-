from django.core.management import BaseCommand
from newsletter.cronjob_start_mailings import start_mailing


class Command(BaseCommand):

    def handle(self, *args, **options):
        start_mailing()

