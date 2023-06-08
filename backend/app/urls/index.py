from django.urls import path
from app.views.test import test


urlpatterns = [
    path('test/', test)
]