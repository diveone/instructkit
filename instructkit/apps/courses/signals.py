from .models import BaseModule
from django.db.models.signals import pre_init
from django.dispatch import receiver


# @receiver(pre_init, sender=BaseModule)
# def calculate_duration(sender, *args, **kwargs):
#     duration = kwargs.get('end') - kwargs.get('start')
#     kwargs['duration'] = duration.days
