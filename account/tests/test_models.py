from django.test import TestCase
from ..models import Account, History

class AccountTestCase(TestCase):

    def setUp(self):
        self.account = Account(number='123', initial_value=0)

    def test_str(self):
        self.assertEquals(str(self.account), self.account.number)


class HistoryTestCase(TestCase):

    def setUp(self):
        self.test_history = History(short_description='Débito')

    def test_str(self):
        self.assertEquals(str(self.test_history), self.test_history.short_description)

    def test_create_history(self):
        assert isinstance(self.test_history, History)
