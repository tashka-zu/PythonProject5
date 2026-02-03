from django.db import models

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