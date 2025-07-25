from config.models import UUIDFIELD
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(UUIDFIELD, AbstractUser):
    def __str__(self):
        return self.username
