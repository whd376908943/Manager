"""Manager URL Configuration

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

from django.conf.urls import url
from django.contrib import admin
from osapp import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^login/', views.login, name="login"),
    url(r'^user/(?P<userid>[0-9]+)/', views.user_info, name="user_info"),
    url(r'^user/manage/', views.user_manage, name="user_manage"),
    url(r'^user/active/', views.user_active, name="user_active"),
    url(r'^user/del/', views.user_del, name='user_del'),
    url(r'^user/add/', views.user_add, name='user_add'),
    url(r'^user/change/', views.user_change, name='user_change'),
    url(r'^user/center/', views.user_center, name='user_center'),
    url(r'^user/change_pwd/', views.pwd_change, name="pwd_change"),
    url(r'^noperm/', views.noperm, name='noperm'),
    url(r'^logout/', views.logout, name="logout")
]
