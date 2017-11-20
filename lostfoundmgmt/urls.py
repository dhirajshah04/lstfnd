from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/'\
        r'(?P<post>[-\w]+)/$',
        views.post_detail,
        name='post_detail'),
    url(r'post/new/$', views.post_new, name='post_new'),
    url(r'^user/dashboard/$', views.dashboard, name='dashboard'),
    url(r'^user/dashboard/myposts/$', views.dash_post_list, name='dash_post_list'),
]
