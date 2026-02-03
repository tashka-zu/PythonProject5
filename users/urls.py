from django.urls import path
from .views import PaymentListView, UserRegistrationView, CreatePaymentView

urlpatterns = [
    path('payments/', PaymentListView.as_view(), name='payment-list'),
    path('register/', UserRegistrationView.as_view(), name='user-register'),
    path('create-payment/', CreatePaymentView.as_view(), name='create-payment'),
]
