// src/main.js
import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import { createPinia } from 'pinia';
import './index.css';
import axios from 'axios';
import { useAuthStore } from './store/authStore';

axios.defaults.baseURL = 'http://localhost:8000';
const app = createApp(App);

const pinia = createPinia();

app.use(pinia);
app.use(router);

const authStore = useAuthStore();
axios.interceptors.request.use((config) => {
    const token = authStore.accessToken;
    if (token) {
        config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
});

app.mount('#app');
