from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser,UserHistory,UserProfileModel
from .serializer import CustomUserSerializer,UserProfileModelSerializer,UserHistorySerializer,UserPassWordVerification,PassWordValidation,LoginSerializer
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
class UserCreationView(APIView):
    def post(self,request):
        data = request.data
        userserializer = CustomUserSerializer(data=data)
        if userserializer.is_valid(raise_exception=True):
            userserializer.save()
            context = {
                 'message':"Registration successfull",
                 "data": userserializer.data
                 }
            return Response(context,status=status.HTTP_201_CREATED)
        else:
            return Response(userserializer.errors, status=status.HTTP_401_UNAUTHORIZED)
        
        return Response({'message':'error occured'}, status=status.HTTP_400_BAD_REQUEST)

class UserHistoryView(APIView):
    def get(self, request):
        data = UserHistory.objects.all()
        historyserializer = UserHistorySerializer(instance=data, many=True)
        return Response(historyserializer.data, status=status.HTTP_200_OK)
       


            
class CreateUserHistory(APIView):
    def post(self,request):
        data = request.data
        created_historyserializer = UserHistorySerializer(data=data)
        if created_historyserializer.is_valid():
            created_historyserializer.save()
            return Response(created_historyserializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(UserHistorySerializer.errors, status=status.HTTP_400_BAD_REQUEST)
        


class GetUserHistory(APIView):
    def get(self, request, pk):
        queryset = UserHistory.objects.filter(user_id=pk)

        if not queryset.exists():
            return Response({'message': 'No matching history records found'}, status=status.HTTP_204_NO_CONTENT)

        serializer = UserHistorySerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

        
    
class EmailVerification(APIView):
    def post(self,request):
        Email = request.data.get('email')
        user_email = CustomUser.objects.filter(email=Email).first()
        if user_email is not None:
             user = CustomUser.objects.get(email=Email)
             userserializer = UserPassWordVerification(user)
             return Response(userserializer.data,status=status.HTTP_200_OK)
        else:
              return Response({'message':'email does not exists in the database'}, status=status.HTTP_404_NOT_FOUND)


class PasswordUpdateView(APIView):
    def put(self,request,pk):
        try:
            user = CustomUser.objects.get(id=pk)
        except user.DoesNotExist:
            return Response({'messsage':' error refresh and try again'},status=status.HTTP_400_BAD_REQUEST)
        
        user_serializer = PassWordValidation(user,data=request.data,partial=True)
        if user_serializer.is_valid(raise_exception=True):
            user_serializer.save()
            return Response({'messsage':'password successfully reset proceed to login'}, status=status.HTTP_200_OK)
        else: 
            return Response(user_serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

class LoginView(APIView):
    def post(self,request):
        data = request.data
        serializer = LoginSerializer(data=data)
        if serializer.is_valid(raise_exception=False):
            email = serializer.validated_data.get('email')
            password = serializer.validated_data.get('password')
            user = authenticate( request=request, email=email, password=password)
            if user is None:
                return Response({ 'message': "Email or Password incorrect"}, status=status.HTTP_401_UNAUTHORIZED)
            else:
                refresh = RefreshToken.for_user(user)
                return Response(
                   {
                'refresh': str(refresh),
                'access': str(refresh.access_token), 
                  },status=status.HTTP_200_OK
                ) 
        else:
            return Response(serializer.error, status=status.HTTP_401_UNAUTHORIZED)


    
class UserAccountModel(APIView):
    def put(self, request, pk):
        user = UserProfileModel.objects.get(user__id = pk)
        if user:
            userserializer = UserProfileModelSerializer(instance=user, data=request.data,partial=True)
            if userserializer.is_valid():
                userserializer.save()
                return Response(userserializer.data, status=status.HTTP_200_OK)
            else:
                return Response(userserializer.errors, status=status.HTTP_401_UNAUTHORIZED)


     


class UsersList(APIView):
    def get(self ,request):
        users = CustomUser.objects.all()
        userserializer = CustomUserSerializer(users, many=True)
        return Response(userserializer.data, status=status.HTTP_200_OK)
    

class UserAccountList(APIView):
    def get(self, request,pk):
        try:
            user= UserProfileModel.objects.get(user__id=pk)
            usermodel = CustomUser.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return Response({'message':'this is the profile of the user '}, status=status.HTTP_400_BAD_REQUEST)
        userseralizer = UserProfileModelSerializer(instance=user)
        usermodelserializer = CustomUserSerializer(instance=usermodel)
        return Response({"account":userseralizer.data,"userinfo":usermodelserializer.data},   status=status.HTTP_200_OK) 
       
       