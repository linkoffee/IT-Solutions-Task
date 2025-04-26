from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import JsonResponse


from .models import (
    Status, OperationType, Category,
    Subcategory, MoneyOperation
)
from .forms import (
    MoneyOperationForm, StatusForm,
    OperationTypeForm, CategoryForm, SubcategoryForm
)
from .filters import MoneyOperationFilter


class OperationListView(ListView):

    model = MoneyOperation
    template_name = 'dds/index.html'
    context_object_name = 'operations'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = MoneyOperationFilter(
            self.request.GET, queryset=queryset
        )
        return self.filterset.qs.order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.filterset
        return context


class OperationCreateView(CreateView):

    model = MoneyOperation
    form_class = MoneyOperationForm
    template_name = 'dds/operation_form.html'
    success_url = reverse_lazy('operation_list')

    def form_valid(self, form):
        messages.success(self.request, 'Операция успешно создана')
        return super().form_valid(form)


class OperationUpdateView(UpdateView):

    model = MoneyOperation
    form_class = MoneyOperationForm
    template_name = 'dds/operation_form.html'
    success_url = reverse_lazy('operation_list')

    def form_valid(self, form):
        return super().form_valid(form)


class OperationDeleteView(DeleteView):

    model = MoneyOperation
    template_name = 'dds/operation_confirm_delete.html'
    success_url = reverse_lazy('operation_list')

    def form_valid(self, form):
        messages.success(self.request, 'Операция успешно удалена')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Удаление операции'
        return context


def load_categories(request):
    type_id = request.GET.get('type_id')
    categories = Category.objects.filter(
        operation_type_id=type_id).order_by('name')
    return JsonResponse(list(categories.values('id', 'name')), safe=False)


def load_subcategories(request):
    category_id = request.GET.get('category_id')
    subcategories = Subcategory.objects.filter(
        category_id=category_id).order_by('name')
    return JsonResponse(list(subcategories.values('id', 'name')), safe=False)


class StatusListView(ListView):

    model = Status
    template_name = 'dds/dictionaries/status_list.html'
    context_object_name = 'statuses'
    paginate_by = 10


class StatusCreateView(CreateView):

    model = Status
    form_class = StatusForm
    template_name = 'dds/dictionaries/status_form.html'
    success_url = reverse_lazy('status_list')

    def form_valid(self, form):
        messages.success(self.request, 'Статус успешно создан')
        return super().form_valid(form)


class StatusUpdateView(UpdateView):

    model = Status
    form_class = StatusForm
    template_name = 'dds/dictionaries/status_form.html'
    success_url = reverse_lazy('status_list')

    def form_valid(self, form):
        messages.success(self.request, 'Статус успешно обновлен')
        return super().form_valid(form)


class StatusDeleteView(DeleteView):

    model = Status
    template_name = 'dds/dictionaries/status_confirm_delete.html'
    success_url = reverse_lazy('status_list')

    def form_valid(self, form):
        messages.success(self.request, 'Статус успешно удален')
        return super().form_valid(form)


class OperationTypeListView(ListView):

    model = OperationType
    template_name = 'dds/dictionaries/type_list.html'
    context_object_name = 'types'
    paginate_by = 10


class OperationTypeCreateView(CreateView):

    model = OperationType
    form_class = OperationTypeForm
    template_name = 'dds/dictionaries/type_form.html'
    success_url = reverse_lazy('type_list')

    def form_valid(self, form):
        messages.success(self.request, 'Тип операции успешно создан')
        return super().form_valid(form)


class OperationTypeUpdateView(UpdateView):

    model = OperationType
    form_class = OperationTypeForm
    template_name = 'dds/dictionaries/type_form.html'
    success_url = reverse_lazy('type_list')

    def form_valid(self, form):
        messages.success(self.request, 'Тип операции успешно обновлен')
        return super().form_valid(form)


class OperationTypeDeleteView(DeleteView):

    model = OperationType
    template_name = 'dds/dictionaries/type_confirm_delete.html'
    success_url = reverse_lazy('type_list')

    def form_valid(self, form):
        messages.success(self.request, 'Тип операции успешно удален')
        return super().form_valid(form)


class CategoryListView(ListView):

    model = Category
    template_name = 'dds/dictionaries/category_list.html'
    context_object_name = 'categories'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        type_id = self.request.GET.get('type_id')
        if type_id:
            queryset = queryset.filter(operation_type_id=type_id)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['types'] = OperationType.objects.all()
        return context


class CategoryCreateView(CreateView):

    model = Category
    form_class = CategoryForm
    template_name = 'dds/dictionaries/category_form.html'
    success_url = reverse_lazy('category_list')

    def form_valid(self, form):
        messages.success(self.request, 'Категория успешно создана')
        return super().form_valid(form)


class CategoryUpdateView(UpdateView):

    model = Category
    form_class = CategoryForm
    template_name = 'dds/dictionaries/category_form.html'
    success_url = reverse_lazy('category_list')

    def form_valid(self, form):
        messages.success(self.request, 'Категория успешно обновлена')
        return super().form_valid(form)


class CategoryDeleteView(DeleteView):

    model = Category
    template_name = 'dds/dictionaries/category_confirm_delete.html'
    success_url = reverse_lazy('category_list')

    def form_valid(self, form):
        messages.success(self.request, 'Категория успешно удалена')
        return super().form_valid(form)


class SubcategoryListView(ListView):

    model = Subcategory
    template_name = 'dds/dictionaries/subcategory_list.html'
    context_object_name = 'subcategories'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.request.GET.get('category_id')
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class SubcategoryCreateView(CreateView):

    model = Subcategory
    form_class = SubcategoryForm
    template_name = 'dds/dictionaries/subcategory_form.html'
    success_url = reverse_lazy('subcategory_list')

    def form_valid(self, form):
        messages.success(self.request, 'Подкатегория успешно создана')
        return super().form_valid(form)


class SubcategoryUpdateView(UpdateView):

    model = Subcategory
    form_class = SubcategoryForm
    template_name = 'dds/dictionaries/subcategory_form.html'
    success_url = reverse_lazy('subcategory_list')

    def form_valid(self, form):
        messages.success(self.request, 'Подкатегория успешно обновлена')
        return super().form_valid(form)


class SubcategoryDeleteView(DeleteView):

    model = Subcategory
    template_name = 'dds/dictionaries/subcategory_confirm_delete.html'
    success_url = reverse_lazy('subcategory_list')

    def form_valid(self, form):
        messages.success(self.request, 'Подкатегория успешно удалена')
        return super().form_valid(form)
