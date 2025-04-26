from django import forms
from django.forms import DateInput
from django.utils import timezone

from .models import (
    Status, OperationType, Category,
    Subcategory, MoneyOperation
)


class MoneyOperationForm(forms.ModelForm):

    class Meta:
        model = MoneyOperation
        fields = '__all__'
        widgets = {
            'created_at': DateInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control'
                },
                format='%Y-%m-%d'
            ),
            'comment': forms.Textarea(
                attrs={'rows': 3, 'class': 'form-control'}
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if not self.instance.pk:
            self.initial['created_at'] = timezone.localdate().strftime('%Y-%m-%d')

        if 'category' in self.data and self.data['category']:
            self.fields['subcategory'].queryset = Subcategory.objects.filter(
                category_id=self.data['category']
            )
        elif self.instance.pk:
            self.fields['subcategory'].queryset = self.instance.category.subcategory_set
        else:
            self.fields['subcategory'].queryset = Subcategory.objects.none()

        for field_name, field in self.fields.items():
            if field_name not in self.Meta.widgets:
                field.widget.attrs['class'] = 'form-control'


class StatusForm(forms.ModelForm):

    class Meta:
        model = Status
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})


class OperationTypeForm(forms.ModelForm):

    class Meta:
        model = OperationType
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})


class SubcategoryForm(forms.ModelForm):

    class Meta:
        model = Subcategory
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
