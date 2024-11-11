from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser): 
    
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

# 
    def __str__(self):
         return self.username
    
#     class isstaff(AbstractUser):
# #     is_staff = models.BooleanField(default=False)
