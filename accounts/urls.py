from django.urls import path
from .views import registro

urlpatterns = [
    path('signup/', registro, name='signup'),
]
