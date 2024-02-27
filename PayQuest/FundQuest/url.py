from django.urls import path
from . import views

urlpatterns =[
    path('FundQuest/', views.FundQuest, name="FundQuests")
]