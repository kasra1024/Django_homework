from rest_framework import serializers
from finance.models import Category , Income , Expense


class IncomeSerializer(serializers.ModelSerializer) : 
    class meta : 
        model = Income
        fields = "__all__"