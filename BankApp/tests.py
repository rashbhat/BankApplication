from django.test import TestCase
from .models import *
# Create your tests here.

class TransDetailsTest(TestCase):

    def test_transaction_fails_on_zero_amount(self):
        account = AccountDetails(account_id=119)
        transaction = TransactionDetails(account_id=account,trans_type='debit',trans_amount=0)
        self.assertEqual(transaction.transaction_succeeded(),False)

class AccountDetailsTest(TestCase):

    def test_account_status(self):
        userBankMap = UserBankMap(userBankMap_id=146)
        account =AccountDetails(userBankMap_id=userBankMap,account_balance=0,account_type='fixed')
        self.assertEqual(account.is_empty(),True)
