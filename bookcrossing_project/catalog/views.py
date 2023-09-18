from django.shortcuts import render

from data import BOOKS


def index_view(request):
    context = {
        'books': BOOKS
    }
    return render(request, 'catalog/index.html', context)


def categories_view(request):
    return render(request, 'catalog/categories.html')


def categories_detail_view(request, id):
    return render(request, 'catalog/category.html')


def book_detail_view(request, id):
    return render(request, 'catalog/book.html')
