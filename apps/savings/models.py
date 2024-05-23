from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class SavingsGoal(models.Model):
    user = models.ForeignKey(User, related_name = "savings", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    target_amount = models.DecimalField(max_digits=10, decimal_places=2)
    current_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    deadline = models.DateField()

    def __str__(self):
        return f"{self.name} - {self.user.username}"

class Deposit(models.Model):
    savings_goal = models.ForeignKey(SavingsGoal, related_name='deposits', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Deposit of {self.amount} to {self.savings_goal.name}"
