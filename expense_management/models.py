# models.py
import uuid

from django.db import models
from django.contrib.auth.models import User


class Group(models.Model):
    models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)


class Member(models.Model):
    models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Expense(models.Model):
    models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid_by = models.ForeignKey(Member, related_name='expenses_paid', on_delete=models.CASCADE)
    group = models.ForeignKey(Group, related_name='expenses', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Settlement(models.Model):
    models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    debtor = models.ForeignKey(Member, related_name='debts', on_delete=models.CASCADE)
    creditor = models.ForeignKey(Member, related_name='credits', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
