from django.urls import path

from product.views.product_view import (
    ProductListView,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
    ProductGTEStockListView,
    ProductLTEStockListView,
)
from product.views.category_view import (
    CategoryListView,
    CategoryDetailView,
    CategoryCreateView,
    CategoryUpdateView,
    CategoryDeleteView,
)
from product.views.supplier_view import (
    SupplierListView,
    SupplierDetailView,
    SupplierCreateView,
    SupplierUpdateView,
    SupplierDeleteView,
    
)


from product.views.product_review_view import (
    ProductReviewCreateView,
    ProductReviewView,
    ProductReviewDetailView,
    ProductReviewUpdateView,
    ProductReviewDeleteView,
)

urlpatterns = [
    # Product URLs
    
    path('products/', ProductListView.as_view(), name='product_list'),
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    path('products/<int:id>/', ProductDetailView.as_view(), name='product_detail'),
    path('products/<int:id>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:id>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('products/gte_stock/', ProductGTEStockListView.as_view(), name='product_gte_stock'),
    path('products/lte_stock/', ProductLTEStockListView.as_view(), name='product_lte_stock'),

    # Category URLs
     path('categories/', CategoryListView.as_view(), name='category_list'),
    path('categories/<int:id>/', CategoryDetailView.as_view(), name='category_detail'),
    path('categories/<int:id>/update/', CategoryUpdateView.as_view(), name='category_update'),
    path('categories/<int:id>/delete/', CategoryDeleteView.as_view(), name='category_delete'),
    path('categories/create/', CategoryCreateView.as_view(), name='category_create'),

    # Product Review URLs
    path('product_reviews/', ProductReviewView.as_view(), name='product_reviews'),
    path('product_reviews/create/', ProductReviewCreateView.as_view(), name='product_reviews_create'),
    path('product_reviews/<int:id>/', ProductReviewDetailView.as_view(), name='product_reviews_detail'),
    path('product_reviews/<int:id>/update/', ProductReviewUpdateView.as_view(), name='product_reviews_update'),
    path('product_reviews/<int:id>/delete/', ProductReviewDeleteView.as_view(), name='product_reviews_delete'),

    # Supplier URLs
    path('suppliers/', SupplierListView.as_view(), name='supplier_list'),
    path('suppliers/<int:id>/', SupplierDetailView.as_view(), name='supplier_detail'),
    path('suppliers/<int:id>/update/', SupplierUpdateView.as_view(), name='supplier_update'),
    path('suppliers/<int:id>/delete/', SupplierDeleteView.as_view(), name='supplier_delete'),
    path('suppliers/create/', SupplierCreateView.as_view(), name='supplier_create'),
]
    
   