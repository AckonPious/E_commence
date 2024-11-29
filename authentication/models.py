from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True, null=False, blank=False)
    username = models.CharField(max_length=150, unique=True, blank=True)
    is_admin = models.BooleanField(default=False)
    USERNAME_FIELD = 'email' 
    REQUIRED_FIELDS = ['username'] 
    
    def save(self, *args, **kwargs):
        if not self.username and self.email:
            self.username = self.email.split('@')[0]
        super().self(*args, **kwargs)
        
    class Meta:
        ordering =  ['username']
        
    def __str__(self):
        return self.username

  