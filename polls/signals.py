from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from polls.models import Choice

LIMIT = 5;


@receiver(pre_save, sender=Choice)
def save_choice(sender, instance, **kwargs):
    if instance.question.choice_set.count() >= LIMIT:
        raise ValueError()
