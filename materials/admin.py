from django.contrib import admin

from users.models import Payment
from .models import Course, Lesson

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    search_fields = ('name',)

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'course', 'description')
    search_fields = ('name', 'course__name')

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'course', 'lesson', 'amount', 'method', 'date')
    search_fields = ('user__email', 'course__name', 'lesson__name')

