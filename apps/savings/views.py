from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import SavingsGoal, Deposit
from .serializers import SavingsGoalSerializer, DepositSerializer
from .permissions import IsOwner

class SavingsGoalViewSet(viewsets.ModelViewSet):
    serializer_class = SavingsGoalSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        return SavingsGoal.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class DepositViewSet(viewsets.ModelViewSet):
    serializer_class = DepositSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        return Deposit.objects.filter(savings_goal__user=self.request.user)

    def perform_create(self, serializer):
        savings_goal = serializer.validated_data['savings_goal']
        savings_goal.current_amount += serializer.validated_data['amount']
        savings_goal.save()
        serializer.save()
