from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.login, name='login'),
    url(r'^ajax/validate_username/$', views.validate_username, name='validate_username'),
    url(r'^signout/$', auth_views.logout, {'next_page': '/'}, name='signout'),
]

