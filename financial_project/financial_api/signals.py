from .models import CustomUser, UserProfileModel,UserHistory
from django.db.models.signals import post_save
from django.dispatch import receiver




@receiver(post_save, sender=CustomUser)
def Create_user_model(sender,instance, created, **kwargs):
    user = instance
    if created:
        userprofile = UserProfileModel.objects.create(user=user)
        userprofile.save()
    print(f'{user.email} created successfully')       

# @receiver(post_save, sender=CustomUser)
# def Create_user_history(sender,instance, created, **kwargs):
#     user = instance
#     if created:
#         userhistory = UserHistory.objects.create(user=user)
#         userhistory.save()
#     print(f'{user.username} created successfully')       
