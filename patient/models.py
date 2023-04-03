from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class Patient(AbstractUser):
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True)
    line1 = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=100)

    groups = models.ManyToManyField(
        Group,
        blank=True,
        related_name='patient_groups'
    )

    user_permissions = models.ManyToManyField(
        Permission,
        blank=True,
        related_name='patient_user_permissions'
    )

    def __str__(self):
        return self.username