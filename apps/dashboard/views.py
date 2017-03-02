from django.shortcuts import render, redirect
from .models import Appointment
from ..appointment.models import User
import datetime

def dashboard(request):
	dateNow=datetime.date.today()
	context= {
		'users': User.objects.filter(id=request.session['id']),
		'appointments': Appointment.objects.filter(user__id=request.session['id']).filter(date=dateNow.strftime('%Y-%m-%d')),
		'other_appointments': Appointment.objects.filter(user__id=request.session['id']).filter(date__gt=dateNow.strftime('%Y-%m-%d')),
		'today_date': dateNow
	}
	return render(request, 'dashboard/dashboard.html', context)
def add_appointment(request):
	if request.method=='POST':
		appointments=Appointment.objects.add_appointment(request.POST['date'], request.POST['time'], request.POST['task'], request.session['id'])
		print appointments
	return redirect('dashboard:dashboard')
def delete(request, id):
	Appointment.objects.delete(id, request.session['id'])
	return redirect('dashboard:dashboard')
def edit(request, id):
	context={
		'appointments': Appointment.objects.filter(id=id),
	}
	return render(request, 'dashboard/edit.html', context)
def update(request, id):
	Appointment.objects.update(id, request.POST['task'], request.POST['status'], request.POST['date'], request.POST['time'])
	return redirect('dashboard:dashboard')
def logout(request):
	request.session.flush()
	return redirect('home:index')