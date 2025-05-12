<template>
  <div style="padding: 50px;" class="container py-4">
    <h1 class="text-center mb-4">📚 Book Management System</h1>

    <nav class="mb-4">
      <router-link style="margin-right: 20px;" to="/" class="btn btn-outline-primary me-2">Home</router-link>
      <router-link style="margin-right: 20px;" to="/books" class="btn btn-outline-primary me-2">Manage Books</router-link>
      <router-link style="margin-right: 20px;" to="/borrow" class="btn btn-outline-primary me-2">Borrow Book</router-link>
      <router-link style="margin-right: 20px;" to="/transactions" class="btn btn-outline-primary me-2">View Transactions</router-link>
      <router-link style="margin-right: 20px;" to="/return-management" class="btn btn-outline-primary me-2">Return Books</router-link>
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
a {
  text-decoration: none;
  color: rgb(255, 255, 255);
  background-color: rgb(86, 86, 86);
  padding: 10px;
  border-radius: 10px;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

a:hover{
  text-decoration: none;
  color: rgb(255, 255, 255);
  background-color: rgb(0, 89, 173);
  padding: 10px;
  border-radius: 10px;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  font-size: 17px;
}

h1{
  font-size: 50px;
}
</style>

