from django.db import models

NULLABLE = {'blank': True, 'null': True}


class ServiceClient(models.Model):
    client_email = models.EmailField(verbose_name='email', unique=True)
    client_name = models.CharField(max_length=100, verbose_name='ФИО')
    client_comment = models.TextField(verbose_name='коментарий')
    mailing = models.ManyToManyField('Mailing')

    def __str__(self):
        return self.client_email

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'


class Mailing(models.Model):
    PERIOD_DAILY = 'daily'
    PERIOD_WEEKLY = 'weekly'
    PERIOD_MONTHLY = 'monthly'

    PERIODS = (
        (PERIOD_DAILY, 'Ежедневная'),
        (PERIOD_WEEKLY, 'Еженедельная'),
        (PERIOD_MONTHLY, 'Ежемесячная'),
    )

    STATUS_CREATED = 'created'
    STATUS_STARTED = 'started'
    STATUS_DONE = 'done'

    STATUSES = (
        (STATUS_CREATED, 'Создана'),
        (STATUS_STARTED, 'Запушена'),
        (STATUS_DONE, 'Завершена')
    )

    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    period = models.CharField(default=PERIOD_WEEKLY, max_length=20,
                              choices=PERIODS, verbose_name='Периодичность рассылки')
    status = models.CharField(default=STATUS_CREATED, max_length=20, choices=STATUSES, verbose_name='Статус рассылки')
    subject_letter = models.CharField(max_length=150, verbose_name='Тема рассылки', **NULLABLE)
    body_letter = models.TextField(verbose_name='Текс рассылки', **NULLABLE)

    def __str__(self):
        return f'{self.subject_letter}'

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'


class MailingLog(models.Model):

    time_last_try = models.DateTimeField(auto_now=True)
    status_log = models.BooleanField(verbose_name='статус отправки рассылки')
    server_response = models.CharField(max_length=150, **NULLABLE)
    client = models.ForeignKey(ServiceClient, on_delete=models.CASCADE, verbose_name='клиент', **NULLABLE)
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, verbose_name='рассылка')

    def __str__(self):
        return self.time_last_try, self.status_log, self.client, self.mailing

    class Mete:
        verbose_name = 'лог рассылки'
        verbose_name_plural = 'логи рассылки'
