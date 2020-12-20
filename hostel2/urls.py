from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name = 'landing_page'),
    path('home/', views.home, name = "home_page"),
    path('gallery/', views.gallery, name="gallery"),
    path('contactus/', views.legend , name="contactus"),
    path('legend/', views.contactus , name="legend"),

]
