<template>
    <form @submit.prevent="handleSubmit">
      <div class="form-group">
        <label>Title</label>
        <input v-model="book.title" class="form-control" required>
      </div>
      <div class="form-group">
        <label>Author</label>
        <input v-model="book.author" class="form-control" required>
      </div>
      <div class="form-group">
        <label>ISBN</label>
        <input v-model="book.isbn" class="form-control" required>
      </div>
      <div class="form-group">
        <label>Copies Available</label>
        <input v-model.number="book.copies_available" type="number" class="form-control" required>
      </div>
      <button type="submit" class="btn btn-primary">{{ book.id ? 'Update' : 'Add' }}</button>
      <button type="button" @click="$emit('cancel')" class="btn btn-secondary ml-2">Cancel</button>
    </form>
  </template>
  
  <script>
  export default {
    props: ['book'],
    methods: {
      handleSubmit() {
        this.$emit(this.book.id ? 'update' : 'add', this.book);
      }
    }
  }
  </script>
  