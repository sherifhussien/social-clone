"""simplesocial URL Configuration

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

"""
1) the patterns are tested in order
2) all request methods – POST, GET, HEAD, etc. – will be routed to the same function for the same URL.
3)Whenever Django encounters include(), it chops off whatever part of the URL matched up to that point and
  sends the remaining string to the included URLconf for further processing.
4)In Django 1.9+ you should set the app_name attribute,In Django 1.8 you need to pass the namespace parameter to include()
"""
from django.conf.urls import url,include
from django.contrib import admin
from simplesocial import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.HomePage.as_view(),name='home'),
    url(r'^accounts/',include('accounts.urls',namespace='accounts')),
    url(r'^accounts/',include('django.contrib.auth.urls')),
    url(r'^test/$',views.TestPage.as_view(),name='test'),
    url(r'^thanks/$',views.ThanksPage.as_view(),name='thanks'),
]
