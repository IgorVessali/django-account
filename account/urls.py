from django.urls import path
from .views import AccountAPIView, HistoryAPIView


urlpatterns = [
    path('accounts', AccountAPIView.as_view(), name='accounts'),
    path('histories', HistoryAPIView.as_view(), name='histories'), 
]