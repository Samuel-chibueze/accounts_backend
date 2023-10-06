from django.urls import path
from .views import UserCreationView,UserHistoryView,CreateUserHistory,GetUserHistory,EmailVerification,PasswordUpdateView,LoginView,UserAccountModel,UsersList,UserAccountList
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns=[
    path('createuser/', UserCreationView.as_view(), name="createuser"),
        path('userhistory/', UserHistoryView.as_view(), name="userhistroy"),
         path('createhistory/', CreateUserHistory.as_view(), name="createhistroy"),
         path('gethistory/<int:pk>/', GetUserHistory.as_view(), name="gethistroy"),
         path('emailverification', EmailVerification.as_view(), name="EmailVerification"),
         path('userpassword/<int:pk>/', PasswordUpdateView.as_view(), name="userpassword"),
         path('login/', LoginView.as_view(), name="login"),
         path('accountupdate/<int:pk>/', UserAccountModel.as_view(), name="updateaccount"),
         path('userslist/', UsersList.as_view() , name="userslist"),
         path('accountlist/<int:pk>/', UserAccountList.as_view(), name="updateaccount"),
         path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
         path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]

