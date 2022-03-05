from django.urls import path

from webapp.views.products import (
    IndexView,
    ProductDetailView,
    ProductCreateView,
    ProductEditView,
    ProductDeleteView,
)
from webapp.views.reviews import (
    ReviewCreateView,
    ReviewUpdateView,
    ReviewDeleteView,
)

app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_view'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/edit/', ProductEditView.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),

    path('product/<int:pk>/review/add/', ReviewCreateView.as_view(), name='review_add'),
    path('review/<int:pk>/update/', ReviewUpdateView.as_view(), name='review_update'),
    path('review/<int:pk>/delete/', ReviewDeleteView.as_view(), name='review_delete'),
]