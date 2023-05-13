from django.shortcuts import render
from matplotlib.style import context
from .models import Product_type
from django.core.paginator import Paginator
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import Product_typeForm
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.urls import reverse_lazy 



def product(request):
    product_types = Product_type.objects.order_by('-id')
    paginator = Paginator(product_types, 3)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)
    is_paginated = page.has_other_pages()
    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''
    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else: 
        next_url = ''
    context = {'product_types': page, 'is_paginated': is_paginated, 'prev_url': prev_url, 'next_url': next_url, }
    return render(request, 'product/index.html', context=context)

class Product_typeCreate(CreateView):
    model = Product_type
    form_class = Product_typeForm
    template_name = 'product/create_product_type.html'
    success_url = '/product/'

class Product_typeUpdate(UpdateView):
    model = Product_type
    form_class = Product_typeForm
    template_name = 'product/update_product_type.html'
    success_url = '/product/'

class Product_typeDelete(DeleteView):
    model = Product_type
    context_object_name = 'product'
    success_url = reverse_lazy('product_url')
    def form_valid(self, form):
        messages.success(self.request, "Успешно")
        return super(Product_typeDelete, self).form_valid(form)

def Product_type_list(request):
    product_types_list = Product_type.objects.order_by('-id')
    query = request.GET.get('q')
    if query:
        product_types_list = Product_type.objects.filter(
            Q(title__icontains=query)
        ).distinct()
    paginator = Paginator(product_types_list, 3) # 6 posts per page
    page = request.GET.get('page')
    try:
        product_types = paginator.page(page)
    except PageNotAnInteger:
        product_types = paginator.page(1)
    except EmptyPage:
        product_types = paginator.page(paginator.num_pages)
    context = {
        'product_types': product_types
    }
    return render(request, 'product_type/product_type_list.html', context=context)