from django.urls import path
from .views import DepositViewSet, SavingsGoalViewSet


deposit_list = DepositViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

deposit_detail = DepositViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


savings_goal_list = SavingsGoalViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

savings_goal_detail = SavingsGoalViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    path('deposits/', deposit_list, name='deposit-list'),
    path('deposits/<int:pk>/', deposit_detail, name='deposit-detail'),
    path('savings_goals/', savings_goal_list, name='savings-goal-list'),
    path('savings_goals/<int:pk>/', savings_goal_detail, name='savings-goal-detail'),
]
