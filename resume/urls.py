from django.urls import path
from . import views

app_name = 'resume'

urlpatterns = [
    path('', views.scroll, name='scroll'),
    path('ecommerce', views.ecommerce, name='ecommerce'),
]


