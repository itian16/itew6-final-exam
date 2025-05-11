<!-- src/views/BooksView.vue -->
<template>
    <div class="container mt-4">
      <h2>📘 Manage Books</h2>
      <BookList />
    </div>
  </template>
  
  <script>
  import BookList from '../components/BookList.vue'
  export default {
    components: { BookList }
  }
  </script>
  