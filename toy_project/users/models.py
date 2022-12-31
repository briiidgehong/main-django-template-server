from django.db import models
from django.utils import timezone
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, AbstractUser

class UserManager(BaseUserManager):
    def _create_user(self, email, password, is_staff, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')

        now = timezone.now()
        user = self.model(
            email=self.normalize_email(email),
            is_staff=is_staff,
            is_active=True,
            last_login=now,
            joined_at=now,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def get_by_natural_key(self, username):
        return self.get(**{'{}__iexact'.format(self.model.USERNAME_FIELD): username})

    def create_user(self, email, password, **extra_fields):
        return self._create_user(email, password, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, **extra_fields)


class Users(AbstractBaseUser):
    email = models.EmailField('Email', max_length=255, unique=True)
    name = models.CharField('Name', max_length=255, blank=True)
    phone_number = models.CharField("휴대폰번호", max_length=20, null=True, blank=True)
    
    is_staff = models.BooleanField('Is staff', default=False)
    is_active = models.BooleanField('Is active', default=True)
    joined_at = models.DateTimeField('Joined at', default=timezone.now)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'Users'