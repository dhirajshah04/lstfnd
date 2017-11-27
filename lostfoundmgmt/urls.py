from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'post/new/$', views.post_new, name='post_new'),
    url(r'^$', views.post_list, name='post_list'),
    url(r'^user/dashboard/$', views.dashboard, name='dashboard'),
    url(r'^user/dashboard/myposts/$', views.dash_post_list, name='dash_post_list'),
    url(r'^about/$', views.about, name='about'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'(?P<slug>[\w-]+)/delete/$', views.post_remove, name='post_remove'),
    url(r'(?P<slug>[\w-]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'(?P<slug>[\w-]+)/$', views.post_detail, name='post_detail'),

]
