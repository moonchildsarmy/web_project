from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Comments, Employee, Order, Contact
from .forms import ReviewForm, MessageForm, OrderForm,CreateUserForm
from django.core.paginator import Paginator
from django.http import HttpResponseNotFound

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect



def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for' + user)

            return redirect('login')

    context = {'form': form}

    return render(request, 'main/register.html', context)


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'main/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def index(request):
    product = Product.objects.filter(is_active=False)
    return render(request, 'main/home.html', {
        'product_list': product
    })


def products(request):
    product_list = Product.objects.filter(is_active=True)
    # categories = Category.objects.all()
    paginator = Paginator(product_list, per_page=6)

    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    return render(request, 'main/products.html', {
        'product_list': page_obj.object_list,
        # 'categories': categories,
        'paginator': paginator,
        'page_obj': page_obj,
        'page_number': int(page_number),
    })


def product_detail(request, id):
    product = Product.objects.get(id=id)
    form = ReviewForm()

    return render(request, 'main/product_detail.html', {
        'product': product,
        'form': form,


    })


# def product_review(request, pk):
#     form = ReviewForm(request.POST)
#     pro = Product.objects.get(id=pk)
#     if form.is_valid():
#         form = form.save(commit=False)
#         form.pro = pro
#         form.save()
#     return redirect(pro.get_absolute_url())


def add_review(request, pk):
    product = get_object_or_404(Product, id=pk)
    comment = Comments.objects.filter(product=product, moderation=True)
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.product = product
            form.save()
            return redirect(product_detail, pk)
    else:
        form = ReviewForm()
    return render(request, 'main/product_detail.html', {'product': product, 'form': form, 'comment': comment})


def about(request):
    employee = Employee.objects.all()
    return render(request, 'main/about.html', {
        'employee': employee
    })


def contact(request):
    addresses = Contact.objects.all()
    contact = Contact.objects.all().first()
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
    else:
        form = MessageForm()
    return render(request, 'main/contact.html', {
        'form': form,
        'contact': contact,
        'addresses': addresses
    })


def order(request, pk):
    product = get_object_or_404(Product, id=pk)
    order = Order.objects.filter(product=product, moderation=True)
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.product = product
            form.save()
            return redirect(product_detail, pk)
        else:
            form = OrderForm()
        return render(request, 'main/product_detail.html', {'product': product, 'form': form, 'order': order })


def cart(request):
    object = Order.objects.all()
    return render(request, 'main/cart.html', {
        'object': object
    })


def delete(request, id):
    try:
        item = Order.objects.get(id=id)
        item.delete()
        return redirect('cart')
    except Order.DoesNotExist:
        return HttpResponseNotFound("<h2>Товар не найден</h2>")






# def category(request, id):
#     categories = Category.objects.get(id=id)
#     queryset = Product.objects.filter(category=categories)
#
#     if queryset:
#         c = {'item': queryset,
#              }
#         return render(request, 'main/products.html', c)
#     else:
#         return render(request, 'main/products.html')








# Create your views here.
