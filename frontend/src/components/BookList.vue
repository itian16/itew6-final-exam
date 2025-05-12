<template>
    <div style="font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;">
      <table class="table table-bordered" id="booktable">
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
        <button class="btn btn-success mb-2" @click="addMode">Add Book</button>
      </table><br><br>
      <BookForm v-if="showForm" :book="selectedBook" @add="createBook" @update="updateBook" @cancel="cancelForm" />
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

#booktable {
  width: 100%;
  border-collapse: collapse;
  margin: 25px 0;
  font-size: 0.9em;
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.15);
  border-radius: 5px;
  overflow: hidden;
}

#booktable thead tr {
  background-color: #007bff;
  color: #ffffff;
  text-align: left;
}

#booktable th,
#booktable td {
  padding: 12px 15px;
}

#booktable tbody tr {
  border-bottom: 1px solid #dddddd;
}

#booktable tbody tr:nth-of-type(even) {
  background-color: #f3f3f3;
}

#booktable tbody tr:last-of-type {
  border-bottom: 2px solid #007bff;
}

#booktable tbody tr:hover {
  background-color: #e6f2ff;
}
</style>