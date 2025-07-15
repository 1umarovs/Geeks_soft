from django.urls import path
from .views import main_view as views

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
]
