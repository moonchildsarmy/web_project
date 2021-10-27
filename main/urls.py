from django.urls import path
from . import views


urlpatterns = [
    path("register/", views.registerPage, name='register'),
    path("login/", views.loginPage, name='login'),
    path("logout/", views.logoutUser, name='logout'),
    path("", views.index, name='home'),
    path("add_review/<int:pk>", views.add_review, name='add_review'),
    path("about/", views.about, name='about'),
    path("contact/", views.contact, name='contact'),
    path("products/", views.products, name='products'),
    # path("category_products/<int:id>", views.category, name='category'),
    path("product_detail/<int:id>", views.product_detail, name='product_detail'),
    path("order/<int:pk>", views.order, name='order'),
    path("cart/", views.cart, name='cart'),
    path("delete/<int:id>", views.delete, name='delete'),
]