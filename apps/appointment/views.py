from django.shortcuts import render, redirect
from .models import User
def index(request):
	context= {
		'users': User.objects.all(),
	}
	return render(request, 'appointment/index.html', context)
def register(request):
	if request.method == 'POST':
		user = User.objects.register(request.POST['first_name'], request.POST['last_name'], request.POST['email'], request.POST['password'], request.POST['password_confirm'], request.POST['birthday'])
		if 'error' in user:
			print "Not a Valid Registration form"
			return redirect('home:index')
		if 'theuser' in user:
			print "Valid Registration Form"
			return redirect('home:index')	
	return redirect('home:index')
def login(request):
	if request.method == 'POST':
		response=User.objects.login(request.POST['email'], request.POST['password'])
		if 'error' in response:
			print 'invalid login'
			return redirect('home:index')
		if 'theuser' in response:
			print 'successful login'
			user=User.objects.get(email=request.POST['email'])
			request.session['id'] = user.id
			return redirect('dashboard:dashboard')
	return redirect('home:index')