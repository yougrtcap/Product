from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

app_name = 'app'
urlpatterns = [
    path('', views.index, name='index'),
    path('users/<int:pk>', views.users_detail, name='users_detail'),
    path('signup/', views.signup, name='signup'),
    path('photos/new/', views.photos_new, name='photos_new'),
    path('login/', auth_views.LoginView.as_view(template_name='app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
