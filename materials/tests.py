from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from users.models import User
from .models import Course, Lesson, Subscription

class LessonAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='test@example.com', password='testpass')
        self.course = Course.objects.create(name='Test Course', description='Test Description', owner=self.user)
        self.lesson = Lesson.objects.create(
            name='Test Lesson',
            description='Test Description',
            course=self.course,
            owner=self.user
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_create_lesson(self):
        url = reverse('lesson-list-create')
        data = {
            'name': 'New Lesson',
            'description': 'New Description',
            'course': self.course.id,
            'video_link': 'https://www.youtube.com/watch?v=example'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_invalid_video_link(self):
        url = reverse('lesson-list-create')
        data = {
            'name': 'New Lesson',
            'description': 'New Description',
            'course': self.course.id,
            'video_link': 'https://example.com/video'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class SubscriptionAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='test@example.com', password='testpass')
        self.course = Course.objects.create(name='Test Course', description='Test Description', owner=self.user)
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_subscribe_to_course(self):
        url = reverse('course-subscribe')
        data = {'course_id': self.course.id}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(Subscription.objects.filter(user=self.user, course=self.course).exists())

    def test_unsubscribe_from_course(self):
        Subscription.objects.create(user=self.user, course=self.course)
        url = reverse('course-subscribe')
        data = {'course_id': self.course.id}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(Subscription.objects.filter(user=self.user, course=self.course).exists())
