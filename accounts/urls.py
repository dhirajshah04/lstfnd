from django.conf.urls import url
from accounts import views

urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^user/login/$', views.login_view, name='login'),
    url(r'^user/logout/$', views.logout_view, name='logout'),
    url (r'^user/change-password/$', views.change_password, name='change_password'),
]