from django.urls import path
from personal.views import home_screen_view, test

urlpatterns = [
    path('', home_screen_view, name='home'),
    path('test/', test, name='test'),
]
