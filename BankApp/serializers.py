from .models import UserDetails,TransactionDetails
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetails
        fields = ('user_id', 'user_name')
        

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionDetails
        fields = ('trans_id','account_id' ,'trans_type','trans_amount')