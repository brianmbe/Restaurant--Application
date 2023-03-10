from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import User, UserProfile


# creating signals (Automatic user creation) - Post save

@receiver(post_save, sender=User)
def post_save_receiver(sender, instance, created, **kwargs):
    print(created)
    if created:
        UserProfile.objects.create(user=instance)
        print(f"{instance.username} has been created!")
    else:
        try:
            profile = UserProfile.objects.get(user=instance)
            profile.save()
            print('user updated')
        except:
            UserProfile.objects.create(user=instance)
            print('No userfound but user has been created')
        print('user updated!')

# Pre-save


@receiver(pre_save, sender=User)
def profile_pre_save_receiver(sender, instance, **kwargs):
    print('this user is being saved!')
