from django.urls import path
from .views import siteListAPIView,siteRetriveAPIView

urlpatterns = [
    path('all', siteListAPIView.as_view()),
    path('<str:code>',siteRetriveAPIView.as_view())
]