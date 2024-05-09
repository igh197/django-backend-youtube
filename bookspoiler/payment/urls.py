from django.contrib import admin
from django.urls import path,include
from .views import PaymentView
urlpatterns = [
   path('payment/create/<int:user_id>',PaymentView.as_view()),
   path('payments',PaymentView.get_payments),

]