from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Budget(models.Model):
    user:User = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, )
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.name} - {self.user.username}"

class Expense(models.Model):
    budget = models.ForeignKey(Budget, related_name='expenses', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.amount}"
