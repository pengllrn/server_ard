"""server_ard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
import server_login.views as sv

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^Login/(?P<user_id>[A-Za-z0-9]+)/(?P<user_pwd>[A-Za-z0-9]+)/$',sv.ard_login),
    url(r'^server_login/',include('server_login.urls')),
]
