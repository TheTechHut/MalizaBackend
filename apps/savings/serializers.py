from rest_framework import serializers
from .models import SavingsGoal, Deposit

class DepositSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deposit
        fields = ['id', 'savings_goal', 'amount', 'timestamp']

class SavingsGoalSerializer(serializers.ModelSerializer):
    deposits = DepositSerializer(many=True, read_only=True)

    class Meta:
        model = SavingsGoal
        fields = ['id', 'user', 'name', 'target_amount', 'current_amount', 'deadline', 'deposits']
