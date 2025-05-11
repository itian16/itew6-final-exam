<template>
  <div class="return-book">
    <div v-if="loading" class="loading">
      Loading borrowed books...
    </div>
    
    <div v-if="successMessage" class="alert alert-success">
      {{ successMessage }}
    </div>
    
    <div v-if="errorMessage" class="alert alert-danger">
      {{ errorMessage }}
    </div>
    
    <div v-if="!loading && borrowedBooks.length === 0" class="no-books">
      No books are currently borrowed.
    </div>
    
    <table v-if="borrowedBooks.length > 0" class="book-table">
      <thead>
        <tr>
          <th>Book Title</th>
          <th>Author</th>
          <th>ISBN</th>
          <th>Borrowed By</th>
          <th>Borrow Date</th>
          <th>Action</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="transaction in borrowedBooks" :key="transaction.id">
          <td>{{ transaction.book.title }}</td>
          <td>{{ transaction.book.author }}</td>
          <td>{{ transaction.book.isbn }}</td>
          <td>
            {{ getUserDisplay(transaction.user) }}
          </td>
          <td>{{ formatDate(transaction.borrow_date) }}</td>
          <td>
            <button
              @click="returnBook(transaction.id)"
              class="return-btn"
              :disabled="returnInProgress === transaction.id"
            >
              {{ returnInProgress === transaction.id ? 'Returning...' : 'Return Book' }}
            </button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'ReturnBook',
  data() {
    return {
      borrowedBooks: [],
      loading: true,
      successMessage: '',
      errorMessage: '',
      returnInProgress: null
    }
  },
  created() {
    this.fetchBorrowedBooks();
  },
  methods: {
    fetchBorrowedBooks() {
      this.loading = true;
      this.errorMessage = '';
      
      axios.get('transactions/')
        .then(response => {
          this.borrowedBooks = response.data.filter(t => t.status === 'borrowed');
          this.loading = false;
        })
        .catch(error => {
          console.error('Error fetching borrowed books:', error);
          this.errorMessage = 'Failed to load borrowed books. Please try again.';
          this.loading = false;
        });
    },
    
    returnBook(borrowId) {
      this.returnInProgress = borrowId;
      this.successMessage = '';
      this.errorMessage = '';
      
      axios.post(`return/${borrowId}/`)
        .then(response => {
          this.successMessage = 'Book returned successfully!';
          this.fetchBorrowedBooks();
        })
        .catch(error => {
          console.error('Error returning book:', error);
          this.errorMessage = error.response?.data?.error || 'Failed to return the book. Please try again.';
        })
        .finally(() => {
          this.returnInProgress = null;
        });
    },
    
    formatDate(dateString) {
      const date = new Date(dateString);
      return date.toLocaleDateString() + ' ' + date.toLocaleTimeString();
    },

    getUserDisplay(user) {
      if (typeof user === 'string') {
        return user;
      } else if (user && typeof user === 'object') {
        if (user.username && user.email) {
          return `${user.username} (${user.email})`;
        } else if (user.username) {
          return user.username;
        } else if (user.email) {
          return user.email;
        } else if (user.id) {
          return `User #${user.id}`;
        }
      }
      return 'Unknown User';
    }
  }
}
</script>

<style scoped>
.return-book {
  max-width: 1000px;
  margin: 0 auto;
}

.alert {
  padding: 10px;
  margin-bottom: 15px;
  border-radius: 4px;
}

.alert-success {
  background-color: #d4edda;
  color: #155724;
  border: 1px solid #c3e6cb;
}

.alert-danger {
  background-color: #f8d7da;
  color: #721c24;
  border: 1px solid #f5c6cb;
}

.loading, .no-books {
  text-align: center;
  margin: 20px 0;
  font-style: italic;
  color: #666;
}

.book-table {
  width: 100%;
  border-collapse: collapse;
  margin: 25px 0;
  font-size: 0.9em;
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.15);
  border-radius: 5px;
  overflow: hidden;
}

.book-table thead tr {
  background-color: #007bff;
  color: #ffffff;
  text-align: left;
}

.book-table th,
.book-table td {
  padding: 12px 15px;
}

.book-table tbody tr {
  border-bottom: 1px solid #dddddd;
}

.book-table tbody tr:nth-of-type(even) {
  background-color: #f3f3f3;
}

.book-table tbody tr:last-of-type {
  border-bottom: 2px solid #007bff;
}

.book-table tbody tr:hover {
  background-color: #e6f2ff;
}

.return-btn {
  padding: 8px 12px;
  border: none;
  border-radius: 4px;
  background-color: #28a745;
  color: white;
  cursor: pointer;
  transition: background-color 0.3s;
}

.return-btn:hover {
  background-color: #218838;
}

.return-btn:disabled {
  background-color: #6c757d;
  cursor: not-allowed;
}
</style>