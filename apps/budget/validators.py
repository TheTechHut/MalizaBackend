from rest_framework.validators import ValidationError
from .models import Budget, Expense

def validate_budget_data(data):
    if data['budget'] < 0:
        raise ValidationError('Budget cannot be negative')
    if data['budget'] > 100000:
        raise ValidationError('Budget cannot be greater than 100000')
    return data

def validate_expense_data(data):
    if data['amount'] < 0:
        raise ValidationError('Amount cannot be negative')
    if data['amount'] > 100000:
        raise ValidationError('Amount cannot be greater than 100000')
    return data

def validate_budget_exists(data):
    if not Budget.objects.filter(id=data['budget']).exists():
        raise ValidationError('Budget does not exist')
    return data

def validate_expense_exists(data):
    if not Expense.objects.filter(id=data['expense']).exists():
        raise ValidationError('Expense does not exist')
    return data




