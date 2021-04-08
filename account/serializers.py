from rest_framework.serializers import ModelSerializer, SerializerMethodField, PrimaryKeyRelatedField, ValidationError
from .models import Account, History
from django.db.models import Sum



class AccountSerializer(ModelSerializer):

    class Meta:
        model = Account
        fields =  '__all__' 


class HistorySerializer(ModelSerializer):
    
    class Meta:
        model = History
        fields =  ('account','short_description','operation', 'value')

    def validate_value(self, value):  

        if self.initial_data['operation'] =='D':
            return value * -1
        elif self.initial_data['operation'] =='C': 
            return value
        else:
            raise ValidationError('Invalid Operation')
        


class ExtractHistorySerializer(ModelSerializer):

    class Meta:
        model = History
        fields =  ('short_description','operation', 'value', 'date') 


class ExtractSerializer(ModelSerializer):

    histories = ExtractHistorySerializer(many=True, read_only=True)
    current_value = SerializerMethodField()

    class Meta:
        model = Account
        fields = ('number', 'initial_value', 'current_value', 'histories')
        

    def get_current_value(self, obj):
        current_value = obj.histories.aggregate(Sum('value')).get('value__sum')

        if current_value is None:
            return 0

        return current_value + obj.initial_value
