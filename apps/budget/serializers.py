from rest_framework import viewsets
from .models import Expense, Budget
from .permissions import IsOwner
from .validators import validate_expense_exists, validate_budget_exists


class ExpenseSerializer(viewsets.ModelViewSet):
    class Meta:
        model = Expense
        fields = '__all__'

    def validate(self, data):
        validate_expense_exists(self.context['request'].user, data['budget'])
        return data

    def create(self, validated_data):
        expense = Expense.objects.create(**validated_data)
        return expense

    def update(self, instance, validated_data):
        instance.amount = validated_data.get('amount', instance.amount)
        instance.description = validated_data.get('description', instance.description)
        instance.category = validated_data.get('category', instance.category)
        instance.date = validated_data.get('date', instance.date)
        instance.save()
        return instance

    def destroy(self, instance):
        instance.delete()
        return instance

class BudgetSerializer(viewsets.ModelViewSet):
    class Meta:
        model = Budget
        fields = '__all__'

    def validate(self, data):
        validate_budget_exists(self.context['request'].user, data['id'])
        return data

    def create(self, validated_data):
        budget = Budget.objects.create(**validated_data)
        return budget

    def update(self, instance, validated_data):
        instance.amount = validated_data.get('amount', instance.amount)
        instance.save()
        return instance

    def destroy(self, instance):
        instance.delete()
        return instance


