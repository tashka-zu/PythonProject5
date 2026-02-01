from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import UserManager
from materials.models import Course, Lesson
from django.core.validators import MinValueValidator

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Email')
    phone = models.CharField(max_length=35, verbose_name='Телефон', blank=True)
    city = models.CharField(max_length=100, verbose_name='Город', blank=True)
    avatar = models.ImageField(upload_to='avatars/', verbose_name='Аватар', blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

class Payment(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('cash', 'Наличные'),
        ('transfer', 'Перевод на счёт'),
    ]

    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='payments', verbose_name='Пользователь')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата оплаты')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='payments', verbose_name='Оплаченный курс', null=True, blank=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='payments', verbose_name='Оплаченный урок', null=True, blank=True)
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Сумма оплаты',
        validators=[MinValueValidator(0.01)]
    )
    method = models.CharField(max_length=10, choices=PAYMENT_METHOD_CHOICES, verbose_name='Способ оплаты')

    def __str__(self):
        return f"{self.user.email} - {self.amount} ({self.method})"