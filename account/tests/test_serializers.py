from django.test import TestCase
from django.test import Client
from django.urls import reverse_lazy
from ..models import Account, History

import random

class AccountSerializerTestCase(TestCase):

    def setUp(self):
        number = random.randint(0, 100000000)
        self.data = {
            'number' : number,
            'inital_value': 100.33
        }
        self.client = Client()

    def test_account_created(self):
        request = self.client.post(reverse_lazy('accounts'), data= self.data)
        self.assertEquals(request.status_code, 201)


class HistorySerializerTestCase(TestCase):

    def setUp(self):
        account = Account(number="216744", initial_value=0)
        account.save()
        self.data_credit = {
            "account":account.id,
            "short_description": "Test of created",
            "operation": "C",
            "value": 100.33
        }
        self.data_debit = {
            "account":account.id,
            "short_description": "Test of created",
            "operation": "D",
            "value": 100.33
        }
        self.data_err = {
            "account":account.id,
            "short_description": "Test of created",
            "operation": "",
            "value": 100.33
        }
        self.client = Client()

    def test_created_history_credit(self):
        request = self.client.post(reverse_lazy('histories'), data=self.data_credit)
        self.assertEquals(request.status_code, 201)

    def test_created_history_debit(self):
        request = self.client.post(reverse_lazy('histories'), data=self.data_debit)
        self.assertEquals(request.status_code, 201)

    def test_created_history_err(self):
        request = self.client.post(reverse_lazy('histories'), data=self.data_err)
        self.assertEquals(request.status_code, 400)


# class ExtractHistorySerializerTestCase(TestCase):

#     def setUp(self):
#         account = Account(number="216744", initial_value=100)
#         account.save()
#         history = History(account=account, short_description="Test of created", operation='C', value=200.33)
#         self.data_credit = {
#             "account":account.id,
#             "short_description": "Test of created",
#             "operation": "C",
#             "value": 100.33
#         }
#         self.data_debit = {
#             "account":account.id,
#             "short_description": "Test of created",
#             "operation": "D",
#             "value": 100.33
#         }
#         self.client = Client()

#     def test_created_history_credit(self):
#         request = self.client.post(reverse_lazy('histories'), data= self.data_credit)
#         self.assertEquals(request.status_code, 201)

#     def test_created_history_debit(self):
#         request = self.client.post(reverse_lazy('histories'), data= self.data_debit)
#         self.assertEquals(request.status_code, 201)