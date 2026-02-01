from django_filters import rest_framework as filters
from rest_framework import generics
from .models import Payment
from .serializers import PaymentSerializer

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


