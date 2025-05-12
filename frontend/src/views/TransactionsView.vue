<template>
  <div style="padding:80px; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;" class="return-management">
    <h2 style="font-size:40px;">All Borrow Transactions</h2>
    <BorrowTransactions />
  </div>
</template>
  
  <script>
  import BorrowTransactions from '../components/BorrowTransactions.vue'
  export default {
    components: { BorrowTransactions }
  }
  </script>
  