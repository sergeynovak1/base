from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, Group, Permission
from django.contrib.auth.models import UserManager as DjangoUserManager
from django.db import models

from .enums import Role


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UserManager(DjangoUserManager):
    def _create_user(self, email, password, commit=True, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        if commit:
            user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        return self._create_user(email, password, role=Role.admin, **extra_fields)


class User(BaseModel, AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, null=True, blank=True)
    role = models.CharField(
        choices=Role.choices,
        max_length=15,
        default=Role.user,
        verbose_name='Роль'
    )
    email = models.EmailField(unique=True)

    objects = UserManager()

    @property
    def is_staff(self):
        return self.role in (Role.admin, Role.staff)

    @property
    def is_superuser(self):
        return self.role == Role.admin

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']

    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions '
                  'granted to each of their groups.',
        related_name='custom_users'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='custom_users'
    )

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
