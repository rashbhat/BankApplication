from django.forms import ModelForm
from BankApp.models import UserDetails,BankDetails
from django import forms


class userForm(ModelForm):
    bankList=[]
    for i in BankDetails.objects.all():
        bankList.append((i.bank_id,i.bank_name))
    bank = forms.ChoiceField(choices=bankList)
    
    class Meta:
        model = UserDetails
        fields =['user_name']
