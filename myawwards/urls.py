from django.urls import re_path as url,include
from . import views  


urlpatterns=[
    url('^$',views.index,name = 'index'),
    url('profile', views.profile, name='profile'),
    url('post/', views.post, name='post'),
    url('account/', include('django.contrib.auth.urls')),
    url('signup/', views.signup, name='signup'),
]