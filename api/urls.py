from django.urls import path

from .views import OficioAPIView

urlpatterns = [
    path('oficios/', OficioAPIView.as_view()),
]