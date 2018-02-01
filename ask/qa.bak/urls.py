
from django.conf.urls import url
from . import views

urlpatterns = [
		# url(r'w+/', views.login, name='login'),
	    url(r'^$', views.test, name='test'),
 ]
