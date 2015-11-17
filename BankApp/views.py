from django.shortcuts import render
from .models import *
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from .forms import userForm
import logging
# Create your views here.

#REST API
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer,TransactionSerializer


logger=logging.getLogger(__name__)

user_id = 0
def listAccounts(request):
    if request.session['user_id']:
        accountList = AccountDetails.objects.filter(userBankMap_id__user_id_id=request.session['user_id'])
    else:                       
        accountList = AccountDetails.objects.all()
    colDict ={'col1':'Account No.','col2':'Account Holder','col3':'Account Type','col4':'Account Balance','col5':'Action'}
    context = {'accountList':accountList,'title':'Account Details','colDict':colDict}
    logger.debug('hello')
    logger.error('hi')
    return render(request,'BankApp/list.html',context)
    
def listBanks(request):
    accountList = AccountDetails.objects.all()
    
    context = {'accountList':accountList}
    return render(request,'BankApp/list.html',context)

def userDetails(request,user_id):
    try:
        user = UserDetails.objects.get(user_id=user_id)
        context = {'user':user}
        return render(request,'BankApp/user.html',context)
    except Exception as e:
        logger.error(e)
        return HttpResponse(e)

def viewTransc(request,account_id):
    transactions = TransactionDetails.objects.filter(account_id=account_id)
    context = {'transactions':transactions}
    return render(request,'BankApp/transactions.html',context)

def addUser(request):
    print(request.POST)
    f = userForm(request.POST)    
    savedUser=f.save()
    userBankMapObj=UserBankMap.objects.create(user_id =savedUser,bank_id=BankDetails.objects.get(bank_id=request.POST['bank']))    
    return HttpResponse('User  '+str(savedUser.user_name)+' added successfully')

def listUsers(request):
    userList= UserDetails.objects.all()
    colDict={'col1':'User ID','col2':'UserName'}
    usrForm = userForm()
    context ={'userList':userList,'colDict':colDict,'title':'User Details','userForm':usrForm}
    return render(request,'BankApp/list.html',context)

def login(request):
    request.session['user_id'] = ''
    try:
        user = UserDetails.objects.get(user_name=request.POST['user_name'])
        print(request.POST['user_pwd'])
        print(user.user_id)
        if user.user_id == int(request.POST['user_pwd']):
            request.session['user_id'] = user.user_id
            print ('session',request.session['user_id'])
            return HttpResponseRedirect(reverse(listAccounts))

        else:
            context={'message':'failed Validation'}
            return render(request,'login.html',context)
    except:
        logger.error('User Not Found')
        return render(request,'login.html',{'message':'User not found'})
    
def logout(request):
    request.session['user_id'] = ''
    context={'message':'User logged out.'}
    return render(request,'login.html',context)
    

'''views for REST API'''
@api_view(['GET', 'PUT', 'DELETE'])
def user_list(request):
    if request.method=='GET':
        userList= UserDetails.objects.all()
        serializer= UserSerializer(userList,many=True)
        return Response(serializer.data)
    elif request.method=='PUT':
        newUser=UserSerializer(data=request.data)
        
        if newUser.is_valid():
            newUser.save()
            return Response(newUser.data)
        
        
        
        
        
@api_view(['GET', 'PUT', 'DELETE'])
def user_details(request,pk):
    try:
        user = UserDetails.objects.get(user_id=pk)
        print(user.user_id)
    except UserDetails.DoesNotExist:
        print('exception')
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    elif request.method=='DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
        
        
@api_view(['GET', 'PUT', 'DELETE'])
def transaction_list(request):
    if request.method=='GET':
        transactionList= TransactionDetails.objects.all()
        serializer = TransactionSerializer(transactionList,many=True)
        return Response(serializer.data)
    
    
@api_view(['GET', 'PUT', 'DELETE'])
def transaction_details(request,userId,bankId):
    try:
        if request.method=='GET':
            user=UserDetails.objects.get(user_id=userId)
            bank = BankDetails.objects.get(bank_id=bankId)
            UserBank_map = UserBankMap.objects.get(user_id=user,bank_id=bank)
            account= AccountDetails.objects.get(userBankMap_id=UserBank_map)
            transaction = TransactionDetails.objects.filter(account_id=account)        
            serializer = TransactionSerializer(transaction,many=True)
            return Response(serializer.data)
                          
    except Exception as e:
        print(e)
        return Response(status=status.HTTP_404_NOT_FOUND)