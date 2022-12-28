from django.urls import path
from .views import itemListApiView,itemRetrieveAPIView

urlpatterns = [
    path('all', itemListApiView.as_view(), name ="item"),
    path('<str:code>',itemRetrieveAPIView.as_view(), name ="item-detail")
                ]