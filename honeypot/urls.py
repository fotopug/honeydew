from django.conf.urls import url

from . import views

app_name = 'honeypot'
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^(?P<store_id>[0-9]+)/$', views.welcome, name='welcome'),
	url(r'^(?P<store_id>[0-9]+)/thanks/$', views.thanks, name='thanks'),
]
