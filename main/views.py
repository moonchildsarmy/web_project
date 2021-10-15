from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Comments, Employee
from .forms import ReviewForm, MessageForm
from django.core.paginator import Paginator


def index(request):
    product = Product.objects.filter(is_active=False)
    return render(request, 'main/home.html', {
        'product_list': product
    })


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
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
    else:
        form = MessageForm()
    return render(request, 'main/contact.html', {
        'form': form,
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


def product_detail(request, id):
    product = Product.objects.get(id=id)
    form = ReviewForm()
    return render(request, 'main/product_detail.html', {
        'product': product,
        'form': form

    })


def product_review(request, pk):
    form = ReviewForm(request.POST)
    pro = Product.objects.get(id=pk)
    if form.is_valid():
        form = form.save(commit=False)
        form.pro = pro
        form.save()
    return redirect(pro.get_absolute_url())
# Create your views here.
