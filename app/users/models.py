from django.db import models
from django.contrib.auth.models import (AbstractBaseUser,PermissionsMixin,BaseUserManager)
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self,email,password):
        if not email:
            raise ValueError('Please enteer your email')
        user = self.model(email=email)
        user.set_password(password)
        user.save(using=self._db)

        return user


    def create_superuser(self,email,password):
        if not email:
            raise ValueError('Please enter your email')
        user = self.create_user(email,password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using = self._db)

        return user
    

class User(AbstractBaseUser,PermissionsMixin):
    email = models.CharField(max_length=255,unique=True)
    nickname = models.CharField(max_length=255)
    is_business = models.BooleanField(default=False)

    is_active=models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    USERNAME_FIELD='email'

    objects = UserManager()

    def __str__(self):
        return f'email: {self.email}, nickname:{self.nickname}'