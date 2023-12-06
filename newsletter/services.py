from django.conf import settings
from django.core.cache import cache

from newsletter.models import Mailing, ServiceClient


def get_cached_model(model):
    if settings.CACHED_ENABLED:
        key = 'category_list'
        subject_list = cache.get(key)
        if subject_list is None:
            subject_list = model.objects
            cache.set(key, subject_list)
    else:
        subject_list = model.objects
    return subject_list

