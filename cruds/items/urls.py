from django.urls import path
from .views import itemListApiView

urlpatterns = [
    path('all', itemListApiView.as_view()),
]