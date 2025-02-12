from django.urls import  path
from . import views
  
app_name = 'pages'
urlpatterns = [
    path('', views.index, name='home'),
    path('about/',views.about, name="about"),
    path('contact/',views.contact, name='contact'),
    path('gallery/', views.gallery, name= 'gallery'),
    path('menu/',views.menu,name='menu'),
    path("reservation/", views.reservation, name='reservation')
]
