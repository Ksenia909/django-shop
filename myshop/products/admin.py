from django.contrib import admin
from .models import Product, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}
    list_display = ('id', 'name', 'stock', 'available', 'category')
    list_display_links = ('id', 'name')
    ordering = ['name']
    list_editable = ('stock', 'available')
    list_per_page = 10
    actions = ['make_available', 'make_unavailable']
    search_fields = ['name', 'category__name']
    list_filter = ['category__name', 'available']

    @admin.action()
    def make_available(self, request, queryset):
        count = queryset.update(available=True)
        self.message_user(request, f"{count} products became available.")

    @admin.action()
    def make_unavailable(self, request, queryset):
        count = queryset.update(available=False)
        self.message_user(request, f"{count} products became unavailable.")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('id', 'name', 'slug')
    list_display_links = ('id', 'name')
    ordering = ['name']