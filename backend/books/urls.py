from django.urls import path
from .views import BookViewSet, BorrowTransactionViewSet


urlpatterns = [
    #ENDPOINT NG BOOKS
    path('books/', BookViewSet.as_view({'get': 'list', 'post': 'create'}), name='book-list'),
    path('books/<int:pk>/', BookViewSet.as_view({'get': 'retrieve', 'put': 'update'}), name='book-detail'),
    path('books/<int:pk>/delete/', BookViewSet.as_view({'delete': 'destroy'}), name='book-delete'),
    
    #ENDPOINT NG TRANSACTIONS
    path('transactions/', BorrowTransactionViewSet.as_view({'get': 'list'}), name='transaction-list'),
    path('transactions/<int:pk>/', BorrowTransactionViewSet.as_view({'get': 'retrieve'}), name='transaction-detail'),
    
    #ENDPOINT NG BORROW
    path('borrow/', BorrowTransactionViewSet.as_view({'post': 'create'}), name='borrow-book'),
    path('return/<int:borrow_id>/', BorrowTransactionViewSet.as_view({'post': 'return_book'}), name='return-book'),
]
