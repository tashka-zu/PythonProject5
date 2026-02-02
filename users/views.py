from django_filters import rest_framework as filters
from rest_framework import generics
from .models import Payment
from .serializers import PaymentSerializer, UserRegistrationSerializer


class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = []

class PaymentFilter(filters.FilterSet):
    class Meta:
        model = Payment
        fields = {
            'course': ['exact'],
            'lesson': ['exact'],
            'method': ['exact'],
        }

class PaymentListView(generics.ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = PaymentFilter
    ordering_fields = ['date']


