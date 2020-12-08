from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

class MyUserManagement(BaseUserManager):
	def create_user(self, email, password):
		email = self.normalize_email(email)
		user = self.model(email=email)
		user.set_password(password)
		user.save(using=self._db)
		return user
	def create_superuser(self, email, password):
		email = self.normalize_email(email)
		user = self.model(email=email)
		user.set_password(password)
		user.is_superuser = True
		user.is_active = True
		user.is_staff = True
		user.save(using=self._db)
		return user

class MyUser(AbstractBaseUser, PermissionsMixin):
	email = models.EmailField(unique= True, max_length=50)
	fname = models.CharField(max_length=20, blank=True ,null=True)

	lname = models.CharField(max_length=10, blank=True ,null=True)
	dob = models.CharField(blank=True ,null=True ,max_length=10)



	phone_number = models.CharField(blank=True, null=True, max_length=33)
	# confirmpassword = models.CharField(blank=True, null=True, max_length=33)
	is_active = models.BooleanField(default=False)
	is_staff = models.BooleanField(default=False)
	USERNAME_FIELD = 'email'
	objects = MyUserManagement()
	def __str__(self):
		return str(self.email)
