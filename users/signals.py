from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

@receiver(post_save,sender=User)  # this decorator will call create_profile whenever a new user is created.  # This is a Django signal that gets triggered when a new user object is saved to the database.  # sender is the model that sends the signal, instance is the actual instance of the model that was saved, created is a boolean indicating whether a new object was created or an existing one was updated.  # kwargs are additional keyword arguments that can
def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save,sender=User)
def save_profile(sender,instance, **kwargs):
    instance.profile.save()