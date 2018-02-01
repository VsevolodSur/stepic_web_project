
from django.conf.urls import url
from . import views

urlpatterns = [
		url(r'login/$', views.login, name='login'),
	    url(r'^signup/$', views.signup, name='signup'),
	    url(r'^question/[0-9]+/$', views.question, name='question'),  
	    # url(r'^ask/$', views.login, name='login'),
	    url(r'^popular/$', views.popular, name='popular'),
	    url(r'^new/$', views.new, name='new'),
	    url(r'^$', views.test, name='test'),
 ]
