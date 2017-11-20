from django.conf.urls import url
from accounts import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^user/login/$', views.login_view, name='login'),
    url(r'^user/logout/$', views.logout_view, name='logout'),
    url(r'^user/change-password/$', views.change_password, name='change_password'),
    url(r'^user/profile/edit/$', views.edit, name='profile_edit'),
    url(r'^user/profile/$', views.profile, name='profile'),

    url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
]