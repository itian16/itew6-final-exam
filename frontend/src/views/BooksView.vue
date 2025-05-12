<!-- src/views/BooksView.vue -->
<template>
    <div style="padding:80px; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;" class="container mt-4">
      <h2 style="font-size:40px;">Manage Books <i class="fa-solid fa-book"></i></h2>
      <BookList />
    </div>
  </template>
  
  <script>
  import BookList from '../components/BookList.vue'
  export default {
    components: { BookList }
  }
  </script>
  