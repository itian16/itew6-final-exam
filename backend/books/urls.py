from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, BorrowTransactionViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'transactions', BorrowTransactionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('borrow/', BorrowTransactionViewSet.as_view({'post': 'create'}), name='borrow-book'),
    path('return/<int:borrow_id>/', BorrowTransactionViewSet.as_view({'post': 'return_book'}), name='return-book'),
]
