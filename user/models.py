
from django.db import models
from django.contrib.auth.models import PermissionsMixin,AnonymousUser
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import gettext_lazy as _


from .manager import UserManager




class User(AbstractBaseUser, PermissionsMixin):
    
    phone=models.CharField(_('phone'), max_length=30,unique=True)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('staff'), default=False)
    group=models.CharField( max_length=30,blank=True)
    
    



    objects = UserManager()

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        
        
        
        
        


class problem (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description=models.TextField()
  