from django.core.validators import MinValueValidator
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey('Category', related_name='items', on_delete=models.CASCADE, verbose_name='Категория')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['category']


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Stock(models.Model):
    address = models.CharField(max_length=200, unique=True, verbose_name='адресс')
    products = models.ManyToManyField(Product, through='Position', related_name='stocks')

    def __str__(self):
        return f"Склад на {self.address}"

    class Meta:
        verbose_name = 'Склад'
        verbose_name_plural = 'Склады'


class Position(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE, related_name='positions')
    product = models.ForeignKey(Product, related_name='positions', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=18, decimal_places=2, validators=[MinValueValidator(0)])

    def __str__(self):
        return f"позиция {self.product} в кол-ве {self.quantity} шт."

    class Meta:
        verbose_name = 'Позиция'
        verbose_name_plural = 'Позиции'
