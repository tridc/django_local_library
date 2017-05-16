from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^books/$', views.BookListView.as_view(), name='books'),
    url(r'^books/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
    url(r'^books/(?P<pk>[-\w]+)/renew/$', views.renew_book_librarian, name='renew-book-librarian'),
    url(r'^books/create/$', views.BookCreate.as_view(), name='book-create'),
    url(r'^books/(?P<pk>\d+)/update/$', views.BookUpdate.as_view(), name='book-update'),
    url(r'^books/(?P<pk>\d+)/delete/$', views.BookDelete.as_view(), name='book-delete'),
    url(r'^authors/$', views.AuthorListView.as_view(), name='authors'),
    url(r'^authors/(?P<pk>\d+)$', views.AuthorDetailView.as_view(), name='author-detail'),
    url(r'^authors/create/$', views.AuthorCreate.as_view(), name='author-create'),
    url(r'^authors/(?P<pk>\d+)/update/$', views.AuthorUpdate.as_view(), name='author-update'),
    url(r'^authors/(?P<pk>\d+)/delete/$', views.AuthorDelete.as_view(), name='author-delete'),
    url(r'^mybooks/$', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    url(r'^borrowed/$', views.BorrowedBooksListView.as_view(), name='books-borrowed'),
]
