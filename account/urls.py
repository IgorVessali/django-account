from django.urls import path
from .views import AccountAPIView, HistoryAPIView, ExtractAPIView, ExtractAllAPIView


urlpatterns = [
    path('accounts', AccountAPIView.as_view(), name='accounts'),
    path('histories', HistoryAPIView.as_view(), name='histories'), 
    path('extracts/', ExtractAllAPIView.as_view(), name='extracts'),   
    path('extracts/<str:number>/', ExtractAPIView.as_view(), name='extract'), 
]