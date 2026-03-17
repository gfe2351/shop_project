from django.contrib import admin
from .models import Category, Product, ProductImage
# Register your models here.


# Позволяет редактировать изображения прямо внутри страницы товара
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1 # Количество пустых полей для новых фото

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)} # Автоматически заполняет slug из названия

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # Поля, которые мы видим в списке товаров
    list_display = ['name', 'price', 'stock', 'is_active', 'category']
    # Боковой фильтр
    list_filter = ['category', 'is_active']
    # Поиск по названию
    search_fields = ['name']
    # Быстрое редактирование прямо в списке (удобный бонус)
    list_editable = ['price', 'stock', 'is_active']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductImageInline]