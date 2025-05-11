<template>
    <div class="container mt-4">
      <h3>🔄 Borrow a Book</h3>
  
      <form @submit.prevent="borrowBook">
        <div class="form-group mb-2">
          <label>Select Book</label>
          <select v-model="book_id" class="form-control" required>
            <option disabled value="">-- Choose a book --</option>
            <option v-for="book in books" :key="book.id" :value="book.id" :disabled="book.copies_available === 0">
              {{ book.title }} by {{ book.author }} ({{ book.copies_available }} available)
            </option>
          </select>
        </div>
  
        <div class="form-group mb-3">
          <label>Select User</label>
          <select v-model="username" class="form-control" required>
            <option disabled value="">-- Choose a user --</option>
            <option v-for="user in users" :key="user" :value="user">
              {{ user }}
            </option>
          </select>
        </div>
  
        <button class="btn btn-primary">Borrow Book</button>
      </form>
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
        users: ['juan', 'maria', 'pedro', 'ana', 'jose'] // 🔽 hardcoded dummy users
      }
    },
    mounted() {
      axios.get('books/')
        .then(res => {
          this.books = res.data
        })
        .catch(() => {
          alert("Error fetching books.")
        });
    },
    methods: {
      borrowBook() {
        axios.post('borrow/', {
          book_id: this.book_id,
          username: this.username
        })
        .then(() => {
          alert("Book borrowed successfully!")
          this.book_id = ''
          this.username = ''
          return axios.get('books/')
        })
        .then(res => {
          this.books = res.data
        })
        .catch(err => {
          const message = err.response?.data?.error || "Failed to borrow."
          alert(message)
          console.error(err)
        });
      }
    }
  }
  </script>
  