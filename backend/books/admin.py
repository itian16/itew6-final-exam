from django.contrib import admin
from .models import Book, BorrowTransaction

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'isbn', 'copies_available')
    search_fields = ('title', 'author', 'isbn')
    list_filter = ('copies_available',)

@admin.register(BorrowTransaction)
class BorrowTransactionAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'borrow_date', 'return_date', 'status')
    search_fields = ('user__username', 'book__title')
    list_filter = ('status', 'borrow_date', 'return_date')