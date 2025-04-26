from django.contrib import admin

from .models import (
    Status, OperationType, Category,
    Subcategory, MoneyOperation
)


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(OperationType)
class OperationTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'operation_type')
    list_filter = ('operation_type',)
    search_fields = ('name',)


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'get_operation_type')
    list_filter = ('category', 'category__operation_type')
    search_fields = ('name', 'category__name')

    def get_operation_type(self, obj):
        return obj.category.operation_type

    get_operation_type.short_description = 'Тип операции'


@admin.register(MoneyOperation)
class MoneyOperationAdmin(admin.ModelAdmin):
    list_display = (
        'created_at', 'status', 'operation_type',
        'category', 'subcategory', 'amount'
    )
    list_filter = ('status', 'operation_type', 'category', 'subcategory')
    search_fields = ('comment',)
    date_hierarchy = 'created_at'
