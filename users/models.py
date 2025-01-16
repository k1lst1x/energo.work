from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

class Role(models.TextChoices):
    """Роли пользователей"""
    STUDENT = "STUDENT", "Студент"
    DIRECTOR = "DIRECTOR", "Директор"
    HR = "HR", "HR"
    RECRUITER = "RECRUITER", "Рекрутер"
    PRACTICE_SUPERVISOR = "PRACTICE_SUPERVISOR", "Руководитель практики"

class User(AbstractUser):
    role = models.CharField(
        max_length=50,
        choices=Role.choices,
        default=Role.STUDENT
    )
    email = models.EmailField(
        _('email address'),
        unique=True,
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
