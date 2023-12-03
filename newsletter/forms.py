from django import forms
from newsletter.models import ServiceClient, Mailing


class StyleFormMixin:
    def __init__(self, *args, **qwargs):
        super().__init__(*args, **qwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ServiceClientForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = ServiceClient
        fields = (
            'client_email',
            'client_name',
            'client_comment',
            'mailing',
            'owner'
        )


class MailingForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Mailing
        fields = (
            'start_time',
            'end_time',
            'subject_letter',
            'body_letter',
            'period',
            'owner'
        )
