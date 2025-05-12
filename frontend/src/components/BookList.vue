<template>
    <div>
      <button class="btn btn-success mb-2" @click="addMode">Add Book</button>
      <BookForm v-if="showForm" :book="selectedBook" @add="createBook" @update="updateBook" @cancel="cancelForm" />
  
      <table class="table table-bordered">
        <thead>
          <tr><th>Title</th><th>Author</th><th>ISBN</th><th>Copies</th><th>Actions</th></tr>
        </thead>
        <tbody>
          <tr v-for="book in books" :key="book.id">
            <td>{{ book.title }}</td>
            <td>{{ book.author }}</td>
            <td>{{ book.isbn }}</td>
            <td>{{ book.copies_available }}</td>
            <td>
              <button class="btn btn-warning btn-sm" @click="editBook(book)">Edit</button>
              <button class="btn btn-danger btn-sm" @click="deleteBook(book.id)">Delete</button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </template>
  
  <script>
  import axios from 'axios'
  import BookForm from './BookForm.vue'
  
  export default {
    components: { BookForm },
    data() {
      return {
        books: [],
        selectedBook: null,
        showForm: false,
      }
    },
    methods: {
      fetchBooks() {
        axios.get('books/').then(res => this.books = res.data);
      },
      addMode() {
        this.selectedBook = { title: '', author: '', isbn: '', copies_available: 1 };
        this.showForm = true;
      },
      editBook(book) {
        this.selectedBook = { ...book };
        this.showForm = true;
      },
      createBook(book) {
        axios.post('books/', book).then(() => {
          this.fetchBooks();
          this.showForm = false;
        });
      },
      updateBook(book) {
        axios.put(`books/${book.id}/`, book).then(() => {
          this.fetchBooks();
          this.showForm = false;
        });
      },
      deleteBook(id) {
        axios.delete(`books/${id}/delete/`).then(this.fetchBooks);
      },
      cancelForm() {
        this.showForm = false;
      }
    },
    mounted() {
      this.fetchBooks();
    }
  }
  </script>
  