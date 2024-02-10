from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField

class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')

    def __str__(self):
        return self.name

class Advertisement(models.Model):
    CHOICES = (
        ('moderation', 'На модерацию'),
        ('published', 'Опубликовано'),
        ('rejected', 'Отклонено'),
        ('delete', 'На удаление'),
    )

    photo = models.ImageField(upload_to='users/avatars/', verbose_name='Фотография')
    title = models.CharField(max_length=255,  verbose_name='Заголовок')
    description = models.TextField(blank=True,  verbose_name='Описание')
    author = models.ForeignKey(get_user_model(), related_name='advertisements', on_delete=models.CASCADE, verbose_name='Автор')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    price = models.DecimalField(max_digits=10, decimal_places=2,  verbose_name='Цена')
    status_choices = models.CharField(max_length=255, choices = CHOICES, verbose_name='Статус')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    published_at = models.DateTimeField(blank=True, null=True, verbose_name='Дата-время публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата-время редактирования')


    def save(self, *args, **kwargs):
        if self.status_choices == 'published' and not self.published_at:
            self.published_at = timezone.now()
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Comment(models.Model):
    text = models.TextField(verbose_name='Текст')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='Автор')
    advertisement = models.ForeignKey(Advertisement, on_delete=models.CASCADE, verbose_name='Объявление')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата-время создания')

    def __str__(self):
        return f" {self.author} - '{self.advertisement.title}'"


