from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class UsuarioManager(BaseUserManager, models.Manager):

	def _create_user(self, username, email, password, is_staff, is_superuser, **extra_fields):
		email = self.normalize_email(email)
		if not email:
			raise ValueError('Email es obligatorio')
		user = self.model(username=username, email =email, is_staff=is_staff, is_superuser=is_superuser, **extra_fields)
		user.set_password(password)
		user.save(using=self.db)
		return user

	def create_user(self,username,email, password, **extra_fields):
		return self._create_user(username,email, password, False, False, **extra_fields)

	def create_superuser(self, username, email, password, **extra_fields):
		return self._create_user(username, email, password, True, True, **extra_fields)


class Usuario(AbstractBaseUser, PermissionsMixin):

	username = models.CharField(unique=True, max_length=50)
	email = models.EmailField()

	nombres = models.CharField(max_length=150)
	apellidos = models.CharField(max_length=150)

	is_staff = models.BooleanField(default=False)

	objects = UsuarioManager()

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['email']

	def get_short_name(self):
		return self.username