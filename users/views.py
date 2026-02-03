from django_filters import rest_framework as filters
from rest_framework import generics, status

from .serializers import PaymentSerializer, UserRegistrationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Payment
from materials.models import Course
from services.stripe_service import create_product, create_price, create_checkout_session

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

class CreatePaymentView(APIView):
    def post(self, request, *args, **kwargs):
        course_id = request.data.get('course_id')
        amount = request.data.get('amount')

        course = Course.objects.get(id=course_id)

        product = create_product(course.name)

        price = create_price(product.id, amount)

        session = create_checkout_session(price.id)

        payment = Payment.objects.create(
            user=request.user,
            course=course,
            amount=amount,
            method='transfer',
            stripe_session_id=session.id,
            payment_link=session.url
        )

        return Response({'payment_url': session.url}, status=status.HTTP_201_CREATED)
