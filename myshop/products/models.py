from django.db import models
from django.urls import reverse


class AvailableManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(available=True)


class Product(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='products')

    objects = models.Manager()
    available_manager = AvailableManager()

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        
    def __str__(self):
        return self.name

