<!-- src/views/BorrowView.vue -->
<template>
    <div style="padding:80px; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;" class="container mt-4">
      <h2 style="font-size:40px;">Borrow a Book</h2>
      <BorrowBook />
    </div>
  </template>
  
  <script>
  import BorrowBook from '../components/BorrowBook.vue'
  export default {
    components: { BorrowBook }
  }
  </script>
  