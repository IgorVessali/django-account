from django.urls import path
from .views import AccountAPIView, HistoryAPIView, ExtractAPIView


urlpatterns = [
    path('accounts', AccountAPIView.as_view(), name='accounts'),
    path('histories', HistoryAPIView.as_view(), name='histories'),   
    path('extracts', ExtractAPIView.as_view(), name='extracts'), 
]