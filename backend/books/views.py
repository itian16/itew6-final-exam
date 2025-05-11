from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.contrib.auth.models import User
from .models import Book, BorrowTransaction
from .serializers import BookSerializer, BorrowTransactionSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def destroy(self, request, *args, **kwargs):
        book = self.get_object()
        active_borrows = BorrowTransaction.objects.filter(book=book, status='borrowed').exists()
        if active_borrows:
            return Response(
                {"error": "Cannot delete book that is currently borrowed."},
                status=status.HTTP_400_BAD_REQUEST
            )
        return super().destroy(request, *args, **kwargs)


class BorrowTransactionViewSet(viewsets.ModelViewSet):
    queryset = BorrowTransaction.objects.all().order_by('-borrow_date')
    serializer_class = BorrowTransactionSerializer

    def create(self, request, *args, **kwargs):
        """Handle book borrowing"""
        book_id = request.data.get('book_id')
        username = request.data.get('username')

        if not book_id or not username:
            return Response(
                {"error": "Both book_id and username are required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        book = get_object_or_404(Book, pk=book_id)

        if book.copies_available <= 0:
            return Response(
                {"error": "No copies available for borrowing"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        transaction = BorrowTransaction.objects.create(
            book=book,
            user=user,
            status='borrowed'
        )

        book.copies_available -= 1
        book.save()

        serializer = self.get_serializer(transaction)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'], url_path='return/(?P<borrow_id>[^/.]+)')
    def return_book(self, request, borrow_id=None):
        """Mark a book as returned"""
        transaction = get_object_or_404(BorrowTransaction, pk=borrow_id)

        if transaction.status == 'returned':
            return Response(
                {"error": "This book has already been returned"},
                status=status.HTTP_400_BAD_REQUEST
            )

        transaction.status = 'returned'
        transaction.return_date = timezone.now()
        transaction.save()

        book = transaction.book
        book.copies_available += 1
        book.save()

        serializer = self.get_serializer(transaction)
        return Response(serializer.data)
