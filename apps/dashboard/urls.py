from django.conf.urls import url 
from . import views

urlpatterns = [
	url(r'^$', views.dashboard, name='dashboard'),
	url(r'^add_appointment$', views.add_appointment, name='add_appointment'),
	url(r'^(?P<id>\d+)/delete$', views.delete, name='delete'),
	url(r'^(?P<id>\d+)/edit$', views.edit, name='edit'),
	url(r'^(?P<id>\d+)/update$', views.update, name='update'),
	url(r'^logout$', views.logout, name='logout')
]
