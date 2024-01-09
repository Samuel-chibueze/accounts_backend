from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager

# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
    email = models.EmailField(max_length=80, unique=True)
    username = models.CharField(max_length=45)
    phonenumber = models.CharField(max_length=20)

    objects = CustomUserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)



    def __str__(self):
        return f'{self.email}  {self.id}'

STATUS_FEILD = (
        ("Successful", "Successful"),
        ("Pending", "Pending"),
        ("Cancelled", "Cancelled"),
    )

TRANSACTION_FEILD= (
    ('Withdrawal', 'Withdrawal'),
    ('Deposit', 'Deposit'),
    ('Plan', 'Plan')
)
PLANS_FEILD= (
    ('Starter Plan', 'Starter Plan'),
    ('Pro Plan', 'Pro Plan'),
    ('Advanced Plan', 'Advanced Plan'),
    ('Premium Plan', 'Premium Plan'),
    ('Vip Plan', 'Vip Plan')
)

    
class UserProfileModel(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    Current_balance = models.FloatField(max_length=None, default=0.00)
    Account_balance = models.FloatField(max_length=None, default=0.00)
    Savings_balance = models.FloatField(max_length=None, default=0.00)
    Investment = models.FloatField(max_length=None, default=0.00)


    def __str__(self):
         return f"{self.user.email}"
  


class UserHistory(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    amount = models.FloatField(max_length=20, default=0.00)
    payment_method= models.CharField(max_length=20)
    status = models.CharField(max_length=11,choices=STATUS_FEILD, default="Pending")
    disc = models.CharField(max_length=100, default="user deposit")
    Transaction = models.CharField(max_length=11,choices=TRANSACTION_FEILD)
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.Transaction} {self.user.id}"

class CryptoModel(models.Model):
    bitcoin = models.CharField(default="this is the default crypto available " , max_length=70)
    etherium = models.CharField(default="this is the default crypto available ",max_length=70)
    litecoin = models.CharField(default="this is the default crypto available ", max_length=70)
    usdt = models.CharField(default="this is the default crypto available ", max_length=70)

