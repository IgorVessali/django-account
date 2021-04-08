from rest_framework.generics import ListCreateAPIView, CreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework import filters
from .models import Account, History
from .serializers import AccountSerializer, HistorySerializer, ExtractSerializer
import json


class AccountAPIView(ListCreateAPIView):

    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class HistoryAPIView(CreateAPIView):

    queryset = History.objects.all()
    serializer_class = HistorySerializer    


class ExtractAllAPIView(ListAPIView):

    queryset = Account.objects.all()
    serializer_class = ExtractSerializer


class ExtractAPIView(ListAPIView):

    serializer_class = ExtractSerializer
    search_fields = ['operation']
    filter_backends = (filters.SearchFilter,)
    queryset = Account.objects.all()
    
    def get(self, request, number):
        extract = Account.objects.filter(number=number)
        serializer = ExtractSerializer(extract, many=True)
        return Response(serializer.data)

