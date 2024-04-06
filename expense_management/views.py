from rest_framework import generics, status
from rest_framework.response import Response
from .models import Group, Expense, Settlement, Member
from .serializers import GroupSerializer, ExpenseSerializer, SettlementSerializer


class GroupListCreateView(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class GroupDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class ExpenseCreateView(generics.CreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        group_id = serializer.validated_data.pop('group')
        group = Group.objects.get(pk=group_id)
        amount = serializer.validated_data.get('amount')
        members = serializer.validated_data.pop('members')

        # Calculate share per member
        share_per_member = amount / len(members)

        # Create the expense
        expense = Expense.objects.create(group=group, **serializer.validated_data)

        # Create payments for each member
        for member_id in members:
            Member.objects.create(user_id=member_id, group=group, expense=expense, amount=share_per_member)

        return Response(self.serializer_class(expense).data, status=status.HTTP_201_CREATED)


class SettlementCreateView(generics.CreateAPIView):
    queryset = Settlement.objects.all()
    serializer_class = SettlementSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        debtor_id = serializer.validated_data.get('debtor')
        creditor_id = serializer.validated_data.get('creditor')
        amount = serializer.validated_data.get('amount')

        # Create the settlement
        settlement = Settlement.objects.create(debtor_id=debtor_id, creditor_id=creditor_id, amount=amount)

        return Response(self.serializer_class(settlement).data, status=status.HTTP_201_CREATED)


class SettlementListView(generics.ListAPIView):
    queryset = Settlement.objects.all()
    serializer_class = SettlementSerializer
