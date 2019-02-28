from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название категории')
    slug = models.SlugField(max_length=255, unique=True)
    created_by = models.ForeignKey(User, on_delete='SET_NULL', related_name='category_created_by', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(User, on_delete='SET_NULL', related_name='category_updated_by', blank=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Producer(models.Model):
    category = models.ManyToManyField(Category, related_name='producer_category', verbose_name='Категория')
    name = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product_category', on_delete='Cascade', verbose_name='Категория')
    producer = models.ForeignKey(Producer, related_name='product_producer', on_delete='Cascade', verbose_name='Производитель')
    name = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(max_length=255, unique=True)
    image = models.ImageField(upload_to='static/images/%Y/%m/%d/', verbose_name='Изображение товара')
    description = RichTextField(blank=True, verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    stock = models.PositiveIntegerField(verbose_name="Остаток на складе")
    available = models.BooleanField(default=True, verbose_name="Доступен")
    created_by = models.ForeignKey(User, on_delete='SET_NULL', related_name='product_created_by')
    created = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(User, on_delete='SET_NULL', related_name='product_updated_by')
    updated = models.DateTimeField(auto_now=True)
    sale = models.BooleanField(default=False, verbose_name="Товар по акции?")
    sale_precent = models.PositiveIntegerField(verbose_name='Процент скидки', blank=True, null=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name