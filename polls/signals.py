import datetime

from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.utils import timezone

from polls.models import Choice

LIMIT = 5;


@receiver(pre_save, sender=Choice)
def save_choice(sender, instance, **kwargs):
    if instance._state.adding:
        if instance.question.choice_set.count() >= LIMIT:
            raise ValueError()


@receiver(post_save, sender=Choice)
def extend_closed(sender, instance, **kwargs):
    if instance.question.closed_at:
        instance.question.closed_at += datetime.timedelta(days=1)
        instance.question.save()
    else:
        instance.question.closed_at = timezone.now()
        instance.question.save()
