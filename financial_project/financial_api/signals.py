from .models import CustomUser, UserProfileModel
from django.db.models.signals import post_save
from django.dispatch import receiver




@receiver(post_save, sender=CustomUser)
def Create_user_model(sender,instance, created, **kwargs):
    user = instance
    if created:
        userprofile = UserProfileModel.objects.create(user=user)
        userprofile.save()
    print(f'{user.email} created successfully')       