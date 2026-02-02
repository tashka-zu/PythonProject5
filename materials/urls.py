from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, LessonListCreateView, LessonRetrieveUpdateDestroyView, LessonViewSet, \
    SubscriptionAPIView

router = DefaultRouter()
router.register(r'lessons', LessonViewSet, basename='lessons')
router.register(r'courses', CourseViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('lessons/', LessonListCreateView.as_view(), name='lesson-list-create'),
    path('lessons/<int:pk>/', LessonRetrieveUpdateDestroyView.as_view(), name='lesson-detail'),
    path('subscribe/', SubscriptionAPIView.as_view(), name='course-subscribe'),
    path('', include(router.urls)),
]
