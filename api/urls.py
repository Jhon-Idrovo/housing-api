from django.urls import path
from .views import ExpensesList, ExpenseStats

app_name = 'api'

urlpatterns = [
    path('all-expenses/', ExpensesList.as_view(), name='list'),
    path('statistics/', ExpenseStats.as_view(), name='stats'),
]