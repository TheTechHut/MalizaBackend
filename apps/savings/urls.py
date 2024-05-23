from django.urls import path
from .views import DepositViewSet, SavingsGoalViewSet


urlpatterns = [
  path("deposits/", DepositViewSet.as_view(), name="deposits"),
  path("savings-goals/", SavingsGoalViewSet.as_view(), name="savings-goals"),
]
