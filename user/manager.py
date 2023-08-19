
from django.contrib.auth.base_user import BaseUserManager
from rest_framework.exceptions import APIException
import re
class UserManager(BaseUserManager):
    use_in_migrations = True



   


    def create(self, password=None, **extra_fields):
        pattern = r'^\+\d{3,15}$'

        if not re.match(pattern, extra_fields['phone']):
            raise APIException(detail={"detail":"phone number is unvalid"})
        user = self.model(**extra_fields)

        user.set_password(password)
        user.save(using=self._db)
        return user




    def create_superuser(self, password, **extra_fields):
        user = self.model(**extra_fields)
        user.set_password(password)
        user.is_superuser = True
        user.is_staff = True
        user.active = True
        user.group='admin'
        user.save(using=self._db)

        return user



    def update(self, user_id, **kwargs):

           


            user = self.get(id=user_id)

            for attr, value in kwargs.items():
                setattr(user, attr, value)
            user.set_password(kwargs['password'])

            user.save(using=self._db)

            return user
