from django.urls import path

from polls import views

urlpatterns = [
    path('calculateAnnualClearProfit', views.index, name='index')
]
