from django.urls import path
from .views import dummy, realm

urlpatterns = [
    path('realm/<int:realm_id>', realm),
]
