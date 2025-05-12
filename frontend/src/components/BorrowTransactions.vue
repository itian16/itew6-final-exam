<template>
    <div class="container mt-5">
      <table class="table table-bordered mt-3" id="booktable">
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
  
  <style scoped>
.return-book {
  max-width: 1000px;
  margin: 0 auto;
}

.alert {
  padding: 10px;
  margin-bottom: 15px;
  border-radius: 4px;
}

.alert-success {
  background-color: #d4edda;
  color: #155724;
  border: 1px solid #c3e6cb;
}

.alert-danger {
  background-color: #f8d7da;
  color: #721c24;
  border: 1px solid #f5c6cb;
}

.loading, .no-books {
  text-align: center;
  margin: 20px 0;
  font-style: italic;
  color: #666;
}

#booktable {
  width: 100%;
  border-collapse: collapse;
  margin: 25px 0;
  font-size: 0.9em;
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.15);
  border-radius: 5px;
  overflow: hidden;
}

#booktable thead tr {
  background-color: #007bff;
  color: #ffffff;
  text-align: left;
}

#booktable th,
#booktable td {
  padding: 12px 15px;
}

#booktable tbody tr {
  border-bottom: 1px solid #dddddd;
}

#booktable tbody tr:nth-of-type(even) {
  background-color: #f3f3f3;
}

#booktable tbody tr:last-of-type {
  border-bottom: 2px solid #007bff;
}

#booktable tbody tr:hover {
  background-color: #e6f2ff;
}
</style>