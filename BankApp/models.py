from django.db import models

# Create your models here.

class BankDetails(models.Model):
    bank_id =models.AutoField(primary_key=True)
    bank_name = models.CharField(max_length=200)

    def __str__(self):
        return self.bank_name


class UserDetails(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.user_name)

class UserBankMap(models.Model):
    userBankMap_id =models.AutoField(primary_key=True)
    user_id = models.ForeignKey(UserDetails)
    bank_id = models.ForeignKey(BankDetails)


class AccountDetails(models.Model):
    account_id = models.AutoField(primary_key=True)
    account_type = models.CharField(max_length=200)
    userBankMap_id = models.ForeignKey(UserBankMap)
    account_balance = models.IntegerField()

    def is_empty(self):
        if self.account_balance ==0:
            return True
        else:
            return False


class TransactionDetails(models.Model):
    trans_id = models.AutoField(primary_key=True)
    account_id = models.ForeignKey(AccountDetails)
    trans_type = models.CharField(max_length=200)
    trans_amount =models.IntegerField()

    def transaction_succeeded(self):
        if self.trans_amount == 0:
            return False
        else:
            return True
    
    
