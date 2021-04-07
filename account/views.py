from rest_framework.generics import ListCreateAPIView, CreateAPIView
from .models import Account, History
from .serializers import AccountSerializer, HistorySerializer


class AccountAPIView(ListCreateAPIView):

    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class HistoryAPIView(CreateAPIView):

    queryset = History.objects.all()
    serializer_class = HistorySerializer

    