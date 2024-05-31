from .models import Budget, Expense
from rest_framework import serializers
from rest_framework.validators import ValidationError
from django.conf import settings

class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = '__all__'

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'

      