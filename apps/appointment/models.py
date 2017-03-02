from __future__ import unicode_literals
from django.db import models
import re
import bcrypt
from django.contrib import messages

EMAIL_REGEX = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
NAME_REGEX = re.compile(r'(^[a-zA-Z])')
class UserManager(models.Manager):
	def register(self, first_name, last_name, email, password, password_confirm, birthday):
		errors = []
		if len(first_name) < 3:
			errors.append("Must be atleast 2 characters first_name")
		if len(last_name) < 3:
			errors.append("Must be atleast 2 characters last_name")
		if not NAME_REGEX.match(first_name):
			errors.append("First Name must be all characeters")
		if not NAME_REGEX.match(last_name):
			errors.append("Last Name must be all characters")
		if not EMAIL_REGEX.match(email):
			errors.append("Not a Valid Email Format")
		emails = User.objects.filter(email=email)
		if len(emails) > 0:
			errors.append("Email already exists")

		if len(password) < 8:
			errors.append("Password must be atleast 8 characeters long")
		if not password == password_confirm:
			errors.append("Passwords must match")

		print errors
		if errors:
			return {'error': errors}
		else:
			if len(User.objects.all()) == 0:
				hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
				User.objects.create(first_name=first_name, last_name=last_name, email=email, password=hashed, birthday=birthday)
				return {'theuser': errors}
			else:
				hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
				User.objects.create(first_name=first_name, last_name=last_name, email=email, password=hashed, birthday=birthday)
				return {'theuser': errors}
	def login(self, email, password):
		errors = []
		user = User.objects.filter(email= email)
		if len(user) > 0:
			if bcrypt.hashpw(password.encode(), user[0].password.encode()) == user[0].password:
				return {'theuser': "Valid login"}
			else:
				return {"error": "The password and email does not match"}
		else:
			return {"error": "This email does not exist"}
class User(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	password = models.CharField(max_length=1000)
	birthday = models.DateField()
	objects = UserManager()