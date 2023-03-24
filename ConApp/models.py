from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager

# Create your models here.



class MyUserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not username:
            raise ValueError('You must enter your Username.')
        #instentiation
        user = self.model(username=username,
                          email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self, username, email=None, password=None):
        self.user = self.create_user(username=username, email=email, password=password)
        self.user.is_admin = True
        self.user.is_staff = True
        self.user.save()
        return self.user

class MyUser(AbstractBaseUser):
    username = models.CharField(
        unique=True,
        max_length=100,
        blank=False,
        null=False)
    email = models.EmailField(max_length=100, blank=False)
    password = models.CharField(max_length=255, blank=False, null=False)
    date = models.DateField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    PASSWORL_FIELD = 'password'
    objects = MyUserManager()

    def has_perm(self, permission, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
class SamedNotes(models.Model):
    day = models.CharField(max_length=20)
    notes = models.TextField()
    date = models.DateField(blank=True, null=True)
class MamadouNotes(models.Model):
    day = models.CharField(max_length=20)
    notes = models.TextField()
    date = models.DateField(blank=True, null=True)

