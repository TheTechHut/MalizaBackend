from rest_framework.validators import ValidationError
from .models import Budget, Expense

def validate_budget_exists(user, budget_id):
    try:
        Budget.objects.get(user=user, id=budget_id)
    except Budget.DoesNotExist:
        raise ValidationError("Budget does not exist")

def validate_expense_exists(user, expense_id):
    try:
        Expense.objects.get(budget__user=user, id=expense_id)
    except Expense.DoesNotExist:
        raise serializers.ValidationError("Expense does not exist")


