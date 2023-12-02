from django.utils import timezone
from smtplib import SMTPException
from newsletter.models import Mailing, MailingLog
from django.conf import settings
from django.core.mail import send_mail


def send_newsletter():
    mailings = Mailing.objects.all()
    # mailinglog = MailingLog.objects.all()

    for mailing in mailings:
        update_statuses(mailing)
        if mailing.status == 'started':
            clients = mailing.serviceclient_set.all()
            if not len(clients):
                log = MailingLog.objects.create(
                    status_log=False,
                    server_response='Нет подписанных клиентов',
                    mailing=mailing,
                )
                log.save()
            else:

                for client in clients:
                    try:
                        send_mail(
                                subject=mailing.subject_letter,
                                message=mailing.body_letter,
                                from_email=settings.EMAIL_HOST_USER,
                                recipient_list=[client.client_email],
                                fail_silently=False,
                        )
                        mailing.status = 'done'
                        mailing.save()
                    except SMTPException as error:
                        log = MailingLog.objects.create(
                            status_log=False,
                            server_response=f'Возникла ошибка {error}',
                            mailing=mailing,
                            client=client
                        )
                        log.save()
                    else:
                        log = MailingLog.objects.create(
                            status_log=True,
                            server_response=f'Письмо отправлено',
                            mailing=mailing,
                            client=client
                        )
                        log.save()
        else:
            continue


def update_statuses(mailing):
    time_now = timezone.now()
    if mailing.start_time.replace(tzinfo=None) <= time_now < mailing.end_time.replace(tzinfo=None):
        mailing.status = 'started'
        mailing.save()
    elif time_now >= mailing.end_time.replace(tzinfo=None):
        mailing.status = 'done'
        mailing.save()
