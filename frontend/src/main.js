import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import axios from 'axios'

// Set base URL for all axios requests
axios.defaults.baseURL = 'http://localhost:8000/api/'

const app = createApp(App)
app.use(router)
app.mount('#app')
