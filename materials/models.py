from django.db import models
from users.models import User

class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    preview = models.ImageField(upload_to='courses/', verbose_name='Превью', blank=True, null=True)
    description = models.TextField(verbose_name='Описание')
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='Владелец')

    def __str__(self):
        return self.name

class Lesson(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    preview = models.ImageField(upload_to='lessons/', verbose_name='Превью', blank=True, null=True)
    video_link = models.URLField(verbose_name='Ссылка на видео', blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons', verbose_name='Курс')
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='Владелец')

    def __str__(self):
        return self.name


class Subscription(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='Пользователь')
    course = models.ForeignKey('Course', on_delete=models.CASCADE, verbose_name='Курс')

    class Meta:
        unique_together = ('user', 'course')

    def __str__(self):
        return f"{self.user.email} подписан на {self.course.name}"


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Оплаченный курс')
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Сумма оплаты')
    stripe_session_id = models.CharField(max_length=255, verbose_name='ID сессии Stripe')
    payment_link = models.URLField(verbose_name='Ссылка на оплату')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return f"{self.user.email} - {self.amount} - {self.course.name}"