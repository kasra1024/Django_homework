from django.db import models
from django.contrib.auth.models import AbstractUser




class User(AbstractUser) :
    TYPE_USER = (
    (0, "student"),
    (1, "teacher")
    )
    type = models.CharField(max_length=12 , choices=TYPE_USER)