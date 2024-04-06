# splitwise_app/urls.py
from django.urls import path
from .views import GroupListCreateView, GroupDetailView, ExpenseCreateView, SettlementCreateView, SettlementListView

urlpatterns = [
    path('groups/', GroupListCreateView.as_view(), name='group-list-create'),
    path('groups/<int:pk>/', GroupDetailView.as_view(), name='group-detail'),
    path('expenses/', ExpenseCreateView.as_view(), name='expense-create'),
    path('settlements/', SettlementCreateView.as_view(), name='settlement-create'),
    path('settlements/list/', SettlementListView.as_view(), name='settlement-list'),
]
