<template>
    <div class="container mt-5">
      <h3>📄 All Borrow Transactions</h3>
      <table class="table table-bordered mt-3">
        <thead>
          <tr>
            <th>Book</th>
            <th>User</th>
            <th>Status</th>
            <th>Borrowed On</th>
            <th>Returned On</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="t in transactions" :key="t.id">
            <td>{{ t.book.title }}</td>
            <td>{{ t.user.username }}</td>
            <td>{{ t.status }}</td>
            <td>{{ formatDate(t.borrow_date) }}</td>
            <td>{{ t.return_date ? formatDate(t.return_date) : '—' }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </template>
  
  <script>
  import axios from 'axios'
  
  export default {
    data() {
      return {
        transactions: []
      }
    },
    mounted() {
      axios.get('transactions/')
        .then(res => {
          this.transactions = res.data
        })
        .catch(() => {
          alert("Error fetching transactions.")
        })
    },
    methods: {
      formatDate(datetime) {
        return new Date(datetime).toLocaleString()
      }
    }
  }
  </script>
  