// src/main.js
import { createApp } from 'vue';
import App from './App.vue';
import axios from 'axios';

const app = createApp(App);

// Set the base URL for Axios
axios.defaults.baseURL = 'http://localhost:8000/api/';

// Make Axios available globally
app.config.globalProperties.$axios = axios;

app.mount('#app');
