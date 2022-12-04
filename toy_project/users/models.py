from django.db import models
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    phone_number = models.CharField("휴대폰번호", max_length=20, null=True, blank=True)
    created_on = models.DateTimeField("등록일자", auto_now_add=True, null=True, blank=True)
    updated_on = models.DateTimeField("수정일자", auto_now=True, null=True, blank=True)

    class Meta:
        db_table = 'Users'