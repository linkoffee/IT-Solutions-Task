import django_filters

from .models import MoneyOperation


class MoneyOperationFilter(django_filters.FilterSet):

    created_at = django_filters.DateFromToRangeFilter(
        field_name='created_at',
        label='Период создания',
        widget=django_filters.widgets.RangeWidget(
            attrs={'type': 'date'}
        )
    )

    class Meta:
        model = MoneyOperation
        fields = {
            'status': ['exact'],
            'operation_type': ['exact'],
            'category': ['exact'],
            'subcategory': ['exact'],
            'amount': ['exact', 'gte', 'lte'],
        }
