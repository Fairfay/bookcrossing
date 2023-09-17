from django.urls import path

from . import views

urlpatterns = [
    path('categories/', views.categories_view),
    path('categories/<int:id>/', views.categories_detail_view),
    path('books/<int:id>/', views.book_detail_view),
    path('', views.index_view)
]
