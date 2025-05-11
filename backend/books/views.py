from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Book, BorrowTransaction
from .serializers import BookSerializer, BorrowTransactionSerializer
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.utils import timezone

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    def destroy(self, request, *args, **kwargs):
        book = self.get_object()
        # Check if there are any active borrows for this book
        active_borrows = BorrowTransaction.objects.filter(
            book=book, 
            status='borrowed'
        ).exists()
        
        if active_borrows:
            return Response(
                {"error": "Cannot delete book that is currently borrowed."},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        return super().destroy(request, *args, **kwargs)

class BorrowTransactionViewSet(viewsets.ModelViewSet):
    queryset = BorrowTransaction.objects.all()
    serializer_class = BorrowTransactionSerializer
    
    def create(self, request, *args, **kwargs):
        """Handle book borrowing"""
        book_id = request.data.get('book_id')
        user_id = request.data.get('user_id')
        
        # Validate input data
        if not book_id or not user_id:
            return Response(
                {"error": "Both book_id and user_id are required"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Get the book
        book = get_object_or_404(Book, pk=book_id)
        
        # Check if copies are available
        if book.copies_available <= 0:
            return Response(
                {"error": "No copies available for borrowing"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Create borrow transaction
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer.save(
            book=book,
            user_id=user_id,
            status='borrowed'
        ))
        
        # Update book copies_available
        book.copies_available -= 1
        book.save()
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    @action(detail=False, methods=['post'])
    def return_book(self, request, borrow_id=None):
        """Mark a book as returned"""
        try:
            transaction = BorrowTransaction.objects.get(pk=borrow_id)
        except BorrowTransaction.DoesNotExist:
            return Response(
                {"error": "Transaction not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        
        # Check if already returned
        if transaction.status == 'returned':
            return Response(
                {"error": "This book has already been returned"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Update transaction
        transaction.status = 'returned'
        transaction.return_date = timezone.now()
        transaction.save()
        
        # Update book availability
        book = transaction.book
        book.copies_available += 1
        book.save()
        
        serializer = self.get_serializer(transaction)
        return Response(serializer.data)