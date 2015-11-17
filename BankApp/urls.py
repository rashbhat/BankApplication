"""Bank URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from BankApp import views
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$',TemplateView.as_view(template_name='login.html')),
    url(r'^listAccounts/', views.listAccounts, name='listAccounts'),
    url(r'^(?P<user_id>[0-9]+)/userDetails/$',views.userDetails, name ='userDetails'),
    url(r'^(?P<account_id>[0-9]+)/viewTransc/$',views.viewTransc,name='viewTransc'),
    url(r'^addUser/',views.addUser,name='addUser'),
    url(r'^listUsers/', views.listUsers, name='listUsers'),
    url(r'^login/', views.login, name='login'),
    url(r'^logout/',views.logout,name='logout'),
    
    #REST API URL Patterns
    url(r'^users/$',views.user_list),
    url(r'^userDetail/(?P<pk>[0-9]+)/$',views.user_details),
    url(r'^transactions/$',views.transaction_list),
    url(r'^transactionDetail/(?P<userId>[0-9]+)/(?P<bankId>[0-9]+)/$',views.transaction_details),

]
