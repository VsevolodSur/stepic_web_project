"""ask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
# from django.urls import path
from django.conf.urls import include, url
from . import views

urlpatterns = [
    # url(r'^$', views.myroot, name='myroot'),
    url(r'^', include('qa.urls')),
    # url(r'^login/', qa.views.login, name='login'),
    # url(r'^signup/', include('qa.urls')),
    # url(r'^question/[0-9]+/', include('qa.urls')),
    url(r'^ask/', views.ask, name='ask'),
    # url(r'^popular/', include('qa.urls')),
    # url(r'^new/', include('qa.urls')),
    url(r'^polls/', include('polls.urls')),
    # path('^admin/', admin.site.urls),
    url(r'^.*$', views.err404, name='err404'),
]
