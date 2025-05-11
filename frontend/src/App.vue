<template>
  <div class="container py-4">
    <h1 class="text-center mb-4">📚 Book Management System</h1>

    <nav class="mb-4">
      <router-link to="/" class="btn btn-outline-primary me-2">🏠 Home</router-link>
      <router-link to="/books" class="btn btn-outline-primary me-2">📘 Manage Books</router-link>
      <router-link to="/borrow" class="btn btn-outline-primary">🔄 Borrow Book</router-link>
      <router-link to="/transactions" class="btn btn-outline-primary me-2">📄 View Transactions</router-link>
    </nav>

    <router-view />
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
body {
  background-color: #f9f9f9;
}
</style>
