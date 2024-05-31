from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import ExpenseSerializer, BudgetSerializer
from .validators import validate_budget_data, validate_expense_data, validate_budget_exists


# Create your views here.

class BudgetViewSet(viewsets.ModelViewSet):
    serializer_class = BudgetSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.request.user.budgets.all()

    def perform_create(self, serializer):
        data = validate_budget_data(self.request.data)
        serializer.save(user=self.request.user, **data)

    def perform_update(self, serializer):
        data = validate_budget_data(self.request.data)
        serializer.save(**data)

    def perform_destroy(self, instance):
        instance.delete()



class ExpenseViewSet(viewsets.ModelViewSet):
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.request.user.expenses.all()

    def perform_create(self, serializer):
        data = validate_expense_data(self.request.data)
        data = validate_budget_exists(data)
        serializer.save(user=self.request.user, **data)

    def perform_update(self, serializer):
        data = validate_expense_data(self.request.data)
        data = validate_budget_exists(data)
        serializer.save(**data)

    def perform_destroy(self, instance):
        instance.delete()



