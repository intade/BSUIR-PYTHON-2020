from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.post_list, name='post_list'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/'\
            r'(?P<slug_post>[-\w]+)/$',
            views.post_detail,
            name='post_detail'),
    path('new/', views.post_new, name='post_new'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/'\
            r'(?P<slug_post>[-\w]+)/edit/$',
            views.post_edit,
            name='post_edit'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/'\
            r'(?P<slug_post>[-\w]+)/delete/$',
            views.post_delete,
            name='post_delete'),
]

