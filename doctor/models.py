from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class Doctor(AbstractUser):
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True)
    line1 = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=100)

    groups = models.ManyToManyField(
        Group,
        blank=True,
        related_name='doctor_groups'
    )

    user_permissions = models.ManyToManyField(
        Permission,
        blank=True,
        related_name='doctor_user_permissions'
    )

    def __str__(self):
        return self.username


from django.db import models

# Create your models here.
