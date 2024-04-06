# serializers.py
from rest_framework import serializers
from .models import Group, Expense, Settlement


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class ExpenseSerializer(serializers.ModelSerializer):
    members = serializers.ListField(child=serializers.IntegerField())

    class Meta:
        model = Expense
        fields = '__all__'


class SettlementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Settlement
        fields = '__all__'
