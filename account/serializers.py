from rest_framework.serializers import ModelSerializer
from .models import Account, History


class AccountSerializer(ModelSerializer):

    class Meta:
        model = Account
        fields =  '__all__' 


class HistorySerializer(ModelSerializer):
    
    class Meta:
        model = History
        fields =  '__all__' 