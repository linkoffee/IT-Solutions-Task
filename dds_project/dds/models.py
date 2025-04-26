import datetime as dt

from django.db import models
from django.core.validators import MinValueValidator
from django.forms import ValidationError
from django.utils import timezone


class Status(models.Model):

    name = models.CharField(max_length=64, verbose_name='Название статуса')

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'

    def __str__(self):
        return self.name[:20]

    def get_list_fields(self):
        return [self.name]


class OperationType(models.Model):

    name = models.CharField(max_length=64, verbose_name='Тип операции')

    class Meta:
        verbose_name = 'Тип операции'
        verbose_name_plural = 'Типы операций'

    def __str__(self):
        return self.name[:20]

    def get_list_fields(self):
        return [self.name]


class Category(models.Model):

    name = models.CharField(max_length=64, verbose_name='Название категории')
    operation_type = models.ForeignKey(
        OperationType, on_delete=models.CASCADE, verbose_name='Тип операции'
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name[:20]

    def get_list_fields(self):
        return [self.name, self.operation_type]


class Subcategory(models.Model):

    name = models.CharField(
        max_length=64, verbose_name='Название подкатегории'
    )
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name='Категория'
    )

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'

    def __str__(self):
        return self.name[:20]

    def get_list_fields(self):
        return [self.name, self.category]


class MoneyOperation(models.Model):

    created_at = models.DateField(
        default=timezone.localdate,
        verbose_name='Дата создания записи'
    )
    status = models.ForeignKey(
        Status, on_delete=models.PROTECT, verbose_name='Статус'
    )
    operation_type = models.ForeignKey(
        OperationType, on_delete=models.PROTECT, verbose_name='Тип операции'
    )
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, verbose_name='Категория'
    )
    subcategory = models.ForeignKey(
        Subcategory, on_delete=models.PROTECT, verbose_name='Подкатегория'
    )
    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        validators=[MinValueValidator(0.01)],
        verbose_name='Сумма'
    )
    comment = models.TextField(
        blank=True, null=True, verbose_name='Комментарий'
    )

    class Meta:
        verbose_name = 'Денежная операция'
        verbose_name_plural = 'Денежные операции'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.created_at.date()} - {self.amount} ₽ ({self.status})'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def clean(self):
        if isinstance(self.created_at, dt.datetime):
            self.created_at = self.created_at.date()

        if self.created_at > timezone.localdate():
            raise ValidationError(
                {'created_at': 'Дата не может быть в будущем'}
            )
