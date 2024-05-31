from django.urls import path
from .views import BudgetViewSet, ExpenseViewSet

budget_list = BudgetViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
budget_detail = BudgetViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

expense_list = ExpenseViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
expense_detail = ExpenseViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    path('budgets/', budget_list, name='budget-list'),
    path('budgets/<int:pk>/', budget_detail, name='budget-detail'),
    path('expenses/', expense_list, name='expense-list'),
    path('expenses/<int:pk>/', expense_detail, name='expense-detail'),
]
