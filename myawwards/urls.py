from django.urls import re_path as url,include
from . import views  
from rest_framework import routers

router = routers.DefaultRouter()
router.register('profile', views.ProfileViewSet)


urlpatterns=[
    url('^$',views.index,name = 'index'),
    url('profile', views.profile, name='profile'),
    url('post/', views.post, name='post'),
    url('account/', include('django.contrib.auth.urls')),
    url('signup/', views.signup, name='signup'),
    url('update', views.edit_profile, name='edit_profile'),
    url('search/', views.search_project, name='search'),
    url('add', views.addpost, name='add'),
    url('rating/<post>/', views.rating, name='rating'),
    url('api/', include(router.urls)),
    
]