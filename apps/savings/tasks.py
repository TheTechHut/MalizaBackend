from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from .models import Deposit, SavingsGoal

@shared_task
def send_deposit_email(deposit_id):
  deposit = Deposit.objects.get(id=deposit_id)
  subject = f"Deposit of {deposit.amount} made"
  message = f"Deposit of {deposit.amount} made on {deposit.date}"
  send_mail(subject, message, settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER])


@shared_task
def send_savings_goal_email(savings_goal_id):
  savings_goal = SavingsGoal.objects.get(id=savings_goal_id)
  subject = f"Savings goal of {savings_goal.amount} reached"
  message = f"Savings goal of {savings_goal.amount} reached on {savings_goal.date}"
  send_mail(subject, message, settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER])


  