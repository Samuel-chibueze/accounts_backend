from rest_framework import serializers
from .models import CustomUser,UserHistory,UserProfileModel,CryptoModel

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        # fields = '__all__'
        fields=['id','email', 'username', 'phonenumber', 'password']


    def create(self, validated_data):
        password = validated_data.pop('password')
        user = CustomUser(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def validate_phonenumber(self, value):
        if CustomUser.objects.filter(phonenumber=value).exists():
            raise serializers.ValidationError(f"a user with the phonenumber {value} already exist")
        if not value:
            raise serializers.ValidationError('you have not inputted a Phonenumber')
        return value
    
    def validate_first_name(self, value):
        if len(value)== 0:
            raise serializers.ValidationError("you have not inputted a firstname")
        return value
    
    def validate_last_name(self, value):
        if len(value)== 0:
            raise serializers.ValidationError("you have not inputted a lastname")
        return value
    def validate_password(self, value):
        if len(value)== 0:
            raise serializers.ValidationError("password is invalid")
        elif len(value)< 5:
            raise serializers.ValidationError('password is too weak try another password')
        return value


class UserProfileModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserProfileModel
        fields = "__all__"


class UserHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model=UserHistory
        fields ="__all__"



        
class UserPassWordVerification(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields=['id']      
        


class PassWordValidation(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields=['id','password']

    def validate_password(self, value):
         if len(value)== 0:
            raise serializers.ValidationError("password is invalid")
         elif len(value)< 5:
            raise serializers.ValidationError('password is too weak try another password')
         elif not any(char.isupper() for char in value):
             raise serializers.ValidationError('password format not valid')
         return value
    
    def update(self, instance, validated_data):
        password = validated_data.get('password', None)
        if password is not None:
            instance.set_password(password)  # Hash the new password
        instance.save()
        return instance
       


class LoginSerializer(serializers.Serializer):
    email= serializers.EmailField(required=True)
    password = serializers.CharField(required=True)

class CryptoAvailableSerializer(serializers.ModelSerializer):
    class Meta:
        model=CryptoModel
        fields ="__all__"


# class UserHistorySerializer(serializers.Serializer):
#     user = serializers.CharField()
#     amount = serializers.FloatField(max_length=20, default=0.00)
#     payment_method= serializers.CharField(max_length=20)
#     status = serializers.CharField(max_length=11, default="Pending")
#     disc = serializers.CharField(max_length=100, default="user deposit")
#     Transaction = serializers.CharField(max_length=11)
#     created_at = serializers.DateField(auto_now=True)