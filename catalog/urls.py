from django.contrib import admin
from django.urls import path
from . import views

app_name='catalog'

urlpatterns=[
    path('', views.index , name="index"),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),
    path('Authors/', views.AuthorListView.as_view(),name="Authors")
]
urlpatterns += [
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
]

urlpatterns += [
    path('book/<int:pk>/renew/$', views.renew_book_librarian, name='renew-book-librarian'),
]

urlpatterns += [
    path('author/create/', views.AuthorCreate.as_view(), name='author_create'),
    path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author_update'),
    path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author_delete'),
]
