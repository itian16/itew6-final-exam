<template>
  <div style="border: 2px solid #ccc; border-radius: 10px; padding: 30px; width: 50%; background-color: #70d2ff;">
    <div class="container mt-4">
    <div v-if="successMessage" class="alert alert-success">
      {{ successMessage }}
        </div>
  
    <div v-if="errorMessage" class="alert alert-danger">
      {{ errorMessage }}
        </div>
    
      <form @submit.prevent="borrowBook">
        <div class="form-group mb-2">
          <label>Select Book: </label>
          <select v-model="book_id" class="form-control" required>
            <option disabled value="">-- Choose a book --</option>
            <option v-for="book in books" :key="book.id" :value="book.id" :disabled="book.copies_available === 0">
              {{ book.title }} by {{ book.author }} ({{ book.copies_available }} available)
            </option>
          </select>
        </div>

        <div class="form-group mb-3">
          <label>Select User: </label>
          <select v-model="username" class="form-control" required>
            <option disabled value="">-- Choose a user --</option>
            <option v-for="user in users" :key="user" :value="user">
              {{ user }}
            </option>
          </select>
      </div><br>

        <button class="btn btn-primary" :disabled="borrowInProgress">
          {{ borrowInProgress ? 'Borrowing...' : 'Borrow Book' }}
        </button>
      </form>
    </div>
  </div>
  </template>
  
  <script>
  import axios from 'axios'
  
  export default {
    data() {
      return {
        books: [],
        book_id: '',
        username: '',
      users: ['juan', 'maria', 'pedro', 'ana', 'jose'],
      borrowInProgress: false,
      successMessage: '',
      errorMessage: ''
      }
    },
    mounted() {
    this.fetchBooks();
    },
    methods: {
    fetchBooks() {
      axios.get('books/')
        .then(res => {
          this.books = res.data;
        })
        .catch(error => {
          console.error('Error fetching books:', error);
          this.errorMessage = 'Error fetching books. Please try again.';
        });
    },

    borrowBook() {
      this.borrowInProgress = true;
      this.successMessage = '';
      this.errorMessage = '';

      axios.post('borrow/', {
        book_id: this.book_id,
        username: this.username
        })
      .then(() => {
        this.successMessage = "Book borrowed successfully!";
        this.book_id = '';
        this.username = '';
        // ETO LANG PARA I-REFRESH ANG LISTA NG BOOKS SA BORROW PAGE AFTER BORROWING A BOOK
        return this.fetchBooks();
      })
      .catch(err => {
        const message = err.response?.data?.error || "Failed to borrow book.";
        this.errorMessage = message;
        console.error(err);
      })
      .finally(() => {
        this.borrowInProgress = false;
        });
      }
    }
  }
  </script>
  
<style scoped>
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
</style>
