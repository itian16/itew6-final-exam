<!-- src/views/BorrowView.vue -->
<template>
    <div class="container mt-4">
      <h2>🔄 Borrow a Book</h2>
      <BorrowBook />
    </div>
  </template>
  
  <script>
  import BorrowBook from '../components/BorrowBook.vue'
  export default {
    components: { BorrowBook }
  }
  </script>
  