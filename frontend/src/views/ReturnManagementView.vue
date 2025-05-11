<template>
  <div class="return-management">
    <h2>📥 Return Management</h2>
    
    <ReturnBook />
  </div>
</template>

<script>
import ReturnBook from '../components/ReturnBook.vue';

export default {
  name: 'ReturnManagementView',
  components: {
    ReturnBook
  }
}
</script>

<style scoped>

h2 {
  margin-bottom: 20px;
  color: #333;
}

</style>