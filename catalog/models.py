from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название")
    # Уникальность slug обязательна для корректных URL
    slug = models.SlugField(max_length=200, unique=True, verbose_name="URL (Slug)")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name="Категория")
    name = models.CharField(max_length=255, verbose_name="Название")
    slug = models.SlugField(max_length=255, unique=True, verbose_name="URL (Slug)")
    
    # DecimalField — стандарт для цен (защита от ошибок округления)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    description = models.TextField(blank=True, verbose_name="Описание")
    stock = models.PositiveIntegerField(default=0, verbose_name="Остаток на складе")
    is_active = models.BooleanField(default=True, verbose_name="Активен")

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images', verbose_name="Товар")
    image = models.ImageField(upload_to='products/%Y/%m/%d/', verbose_name="Изображение")
    alt_text = models.CharField(max_length=255, blank=True, verbose_name="Текст для SEO")
    is_main = models.BooleanField(default=False, verbose_name="Главное фото")

    class Meta:
        verbose_name = "Изображение товара"
        verbose_name_plural = "Изображения товаров"

    def __str__(self):
        return f"Фото для {self.product.name}"