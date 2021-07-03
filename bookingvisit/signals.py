from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Client_Profil

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Client_Profil.objects.create(pk=instance.id, user=instance)

def save_profile(instance, **kwargs):
    instance.create_profile.save()
