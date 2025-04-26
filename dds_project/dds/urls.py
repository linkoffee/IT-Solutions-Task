from django.urls import path
from . import views

urlpatterns = [
    path('', views.OperationListView.as_view(), name='operation_list'),
    path('create/', views.OperationCreateView.as_view(), name='operation_create'),
    path('<int:pk>/edit/', views.OperationUpdateView.as_view(), name='operation_edit'),
    path('<int:pk>/delete/', views.OperationDeleteView.as_view(), name='operation_delete'),
    path('load-categories/', views.load_categories, name='load_categories'),
    path('load-subcategories/', views.load_subcategories, name='load_subcategories'),
    path('dictionaries/statuses/', views.StatusListView.as_view(), name='status_list'),
    path('dictionaries/statuses/create/', views.StatusCreateView.as_view(), name='status_create'),
    path('dictionaries/statuses/<int:pk>/edit/', views.StatusUpdateView.as_view(), name='status_edit'),
    path('dictionaries/statuses/<int:pk>/delete/', views.StatusDeleteView.as_view(), name='status_delete'),
    path('dictionaries/types/', views.OperationTypeListView.as_view(), name='type_list'),
    path('dictionaries/types/create/', views.OperationTypeCreateView.as_view(), name='type_create'),
    path('dictionaries/types/<int:pk>/edit/', views.OperationTypeUpdateView.as_view(), name='type_edit'),
    path('dictionaries/types/<int:pk>/delete/', views.OperationTypeDeleteView.as_view(), name='type_delete'),
    path('dictionaries/categories/', views.CategoryListView.as_view(), name='category_list'),
    path('dictionaries/categories/types/create/', views.CategoryCreateView.as_view(), name='category_create'),
    path('dictionaries/categories/<int:pk>/edit/', views.CategoryUpdateView.as_view(), name='category_edit'),
    path('dictionaries/categories/<int:pk>/delete/', views.CategoryDeleteView.as_view(), name='category_delete'),
    path('dictionaries/subcategories/', views.SubcategoryListView.as_view(), name='subcategory_list'),
    path('dictionaries/subcategories/types/create/', views.SubcategoryCreateView.as_view(), name='subcategory_create'),
    path('dictionaries/subcategories/<int:pk>/edit/', views.SubcategoryUpdateView.as_view(), name='subcategory_edit'),
    path('dictionaries/subcategories/<int:pk>/delete/', views.SubcategoryDeleteView.as_view(), name='subcategory_delete')
]
