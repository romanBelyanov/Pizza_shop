from django import forms
from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    tel = forms.CharField(max_length=15, required=True)

    class Meta:
        model = User
        fields = ("username", "email", "tel", "password1", "password2")

class Menu(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30, default=None)
    salyami = models.BooleanField(default=None)
    tomato_sauce = models.BooleanField(default=None)
    cheese = models.BooleanField(default=None)
    species = models.BooleanField(default=None)
    bazilik = models.BooleanField(default=None)
    ham = models.BooleanField(default=None)
    ananas = models.BooleanField(default=None)
    price = models.IntegerField(default=None)
    description = models.CharField(max_length=150, default=None)

class Availability(models.Model):
    id = models.IntegerField(primary_key=True)
    salyami = models.IntegerField(default=10)
    tomato_sauce = models.IntegerField(default=10)
    cheese = models.IntegerField(default=10)
    species = models.IntegerField(default=10)
    bazilik = models.IntegerField(default=10)
    ham = models.IntegerField(default=10)
    ananas = models.IntegerField(default=10)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_tg_id = models.IntegerField(default=None)
    tel = models.CharField(max_length=15)