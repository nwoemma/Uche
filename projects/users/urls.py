from django.urls import path
from . import views
  
app_name = 'users'
urlpatterns = [
    path('register/', views.register, name='register'),
    path('set_password/', views.set_password, name = 'set_password'),
    path('complete_profile/<int:user_id>',views.complete_profile, name='complete_profile'),
    path('login_user/',views.login_user, name="login_user"),
    
]
