from django.contrib import admin
from .models import CustomUser,UserHistory,UserProfileModel,CryptoModel
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(UserHistory)
admin.site.register(CryptoModel)
admin.site.register(UserProfileModel)