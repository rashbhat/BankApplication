
from BankApp.models import *
import time

def addBank(bankName='corporation',count=1):
    start= time.time()
    try:
        BankDetails.objects.all().delete()
        list = []
        for i in range(0,count):        
            list.append(BankDetails(bank_name=bankName))
            
        bank = BankDetails.objects.bulk_create(list)
        ret=str(count)+ ' Banks added successfully'
    except Exception as e:
        ret = 'unable to add the banks', e
    finally:
        end = time.time()
        print (end-start)
        print ('hi')
        return ret

def addUser(user='testUser',count=1,bank='hdfc'):
    start= time.time()
    try:
        UserBankMap.objects.all().delete()
        UserDetails.objects.all().delete()
        bankObj = BankDetails.objects.create(bank_name=bank)        
        userBankMapList = []
        for i in range(0,count):
            
            userObj = UserDetails.objects.create(user_name =user)
            userBankMapList.append(UserBankMap(bank_id=bankObj,user_id=userObj))
            
            
        UserBankMap.objects.bulk_create(userBankMapList)
            
        ret= str(count)+ ' Users added successfully'
    except Exception as e:
        ret= 'unable to add the users',e
    finally:
        end = time.time()
        print (end-start)
        print ('hi')
        return ret

def addAccount(acc_type='RD',acc_bal=300,count=1):
    start= time.time()
    try:
        AccountDetails.objects.all().delete()
        UserBankMap.objects.all().delete()
        UserDetails.objects.all().delete()
        BankDetails.objects.all().delete()
        bankObj = BankDetails.objects.create(bank_name ='hdfc')
        userObj = UserDetails.objects.create(user_name ='user')
        userBankMapObj = UserBankMap.objects.create(bank_id=bankObj,user_id=userObj)
        accountList=[]
        for i in range (0,count):
            accountList.append(AccountDetails(userBankMap_id = userBankMapObj,account_type=acc_type,account_balance=acc_bal))
        accountObj = AccountDetails.objects.bulk_create(accountList)
        ret= str(count)+ ' Accounts created successfully'
    
    except Exception as e:
        ret= 'unable to create account',e
    finally:
        end = time.time()
        print (end-start)
        print ('hi')
        return ret

def addTransaction(trans_type='credit',trans_amount=100,count=1):
    start= time.time()
    TransactionDetails.objects.all().delete()
    AccountDetails.objects.all().delete()
    UserBankMap.objects.all().delete()
    UserDetails.objects.all().delete()
    BankDetails.objects.all().delete()
    bankObj = BankDetails.objects.create(bank_name ='hdfc')
    userObj = UserDetails.objects.create(user_name ='user')
    userBankMapObj = UserBankMap.objects.create(bank_id=bankObj,user_id=userObj)
    accountObj= AccountDetails.objects.create(userBankMap_id = userBankMapObj,account_type='savings',account_balance='150')
    try:
        transList =[]
        for i in range(0,count):
            transList.append(TransactionDetails(trans_type=trans_type,trans_amount=trans_amount,account_id=accountObj))
        transObj = TransactionDetails.objects.bulk_create(transList)    
        ret= str(count)+ ' Transactions added successfully'
    except Exception as e:
        ret= 'unable to add transactions',e
    finally:
        end = time.time()
        print (end-start)
        print ('hi')
        return ret
        
