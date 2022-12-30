from django.urls import path
from .views import itemListApiView,itemRetrieveAPIView,siteListAPIView,siteRetriveAPIView

urlpatterns = [
    path('items', itemListApiView.as_view(), name ="item"),
    path('items/<str:code>',itemRetrieveAPIView.as_view(), name ="item-details"),
    path('sites', siteListAPIView.as_view()),
    path('sites/<str:code>',siteRetriveAPIView.as_view(),name ="site-details")
#    path('itemsbysite/<str:code>', ItemSiteView.as_view(), name='item-detail'),
#    path('sitesbyitem/<str:code>', SiteItemView.as_view(), name='site-detail'),
]

                