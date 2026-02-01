from rest_framework import serializers
from .models import Course, Lesson, Subscription
from .validators import validate_video_link


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'name', 'description', 'preview', 'video_link', 'course']
        read_only_fields = ['owner']
        extra_kwargs = {
            'video_link': {'validators': [validate_video_link]}
        }

class CourseSerializer(serializers.ModelSerializer):
    is_subscribed = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ['id', 'name', 'preview', 'description', 'is_subscribed']

    def get_is_subscribed(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return Subscription.objects.filter(user=request.user, course=obj).exists()
        return False


