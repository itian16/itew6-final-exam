from rest_framework import serializers
from .models import Book, BorrowTransaction
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'isbn', 'copies_available', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']
        
    def validate_isbn(self, value):
        if len(value) != 13 and len(value) != 10:
            raise serializers.ValidationError("ISBN must be 10 or 13 characters long")

        instance = getattr(self, 'instance', None)
        if instance is not None:
            if instance.isbn != value and Book.objects.filter(isbn=value).exists():
                raise serializers.ValidationError("A book with this ISBN already exists")
        elif Book.objects.filter(isbn=value).exists():
            raise serializers.ValidationError("A book with this ISBN already exists")

        return value
        
    def validate_copies_available(self, value):
        if value < 0:
            raise serializers.ValidationError("Number of copies must be a positive integer")
        return value

class BorrowTransactionSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    book = BookSerializer(read_only=True)
    user_id = serializers.IntegerField(write_only=True)
    book_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = BorrowTransaction
        fields = ['id', 'user', 'book', 'user_id', 'book_id', 'borrow_date', 'return_date', 'status']
        read_only_fields = ['borrow_date', 'return_date', 'status']
