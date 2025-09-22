from django.db import models
from django.contrib.auth.models import AbstractUser



class CustomerUser(AbstractUser):
    storage_quota = models.IntegerField(default=1024)