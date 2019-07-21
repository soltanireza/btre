from django.urls import path, include

from . import views
# from pages import views

urlpatterns = [
    path('contact',views.contact, name='contact'),
]
