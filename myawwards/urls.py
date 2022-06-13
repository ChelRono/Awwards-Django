from django.urls import re_path as url
from . import views

urlpatterns=[
    url('^$',views.index,name = 'index'),
    url('profile/', user_views.profile, name='profile'),
]