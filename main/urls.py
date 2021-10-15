from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name='home'),
    path("add_review/<int:pk>", views.add_review, name='add_review'),
    path("about/", views.about, name='about'),
    path("contact/", views.contact, name='contact'),
    path("products/", views.products, name='products'),
    # path("category_products/<int:id>", views.category, name='category'),
    path("product_detail/<int:id>", views.product_detail, name='product_detail'),
]