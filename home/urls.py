from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('vision', views.vision, name="vision"),
    path('contact', views.contact, name="contact"),
    path('pintu', views.contact, name="pintu"),
]