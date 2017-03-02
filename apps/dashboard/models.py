from __future__ import unicode_literals
from ..appointment.models import User
from django.db import models
import datetime


class AppointmentManager(models.Manager):
	def add_appointment(self, date, time, task, user_id):
		dateNow=datetime.date.today()
		timeNow=datetime.datetime.now().time()
		if dateNow.strftime('%m/%d/%Y') > date:
			status=3
		elif dateNow.strftime('%m/%d/%Y') == date:
			if timeNow.strftime('%H:%M') > time:
				status=3
			else:
				status=1
		else:
			status=1
		appointment=Appointment.objects.create(task=task, date=date, time=time, status=status)
		User.objects.get(id=user_id).appointments.add(appointment)
	def delete(self, id, user_id):
		Appointment.objects.get(id=id).delete()
		pass
	def update(self, id, task, status, date, time):
		Appointment.objects.filter(id=id).update(task=task, status=status, date=date, time=time)
		pass
		
class Appointment(models.Model):
	task=models.CharField(max_length=1000)
	date=models.DateField()
	time=models.TimeField()	
	status=models.IntegerField()
	user=models.ForeignKey(User, related_name='appointments', null=True)
	objects = AppointmentManager()