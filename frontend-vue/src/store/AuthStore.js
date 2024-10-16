import { defineStore } from 'pinia';
import axios from 'axios';

export const useAuthStore = defineStore('auth', {
    state: () => ({
        user: null,
        accessToken: localStorage.getItem('accessToken') || null,
        refreshToken: localStorage.getItem('refreshToken') || null,
    }),
    actions: {
        async login(credentials) {
            try {
                const response = await axios.post('/api/token/', credentials);
                this.accessToken = response.data.access;
                this.refreshToken = response.data.refresh;

                localStorage.setItem('accessToken', this.accessToken);
                localStorage.setItem('refreshToken', this.refreshToken);

                this.user = { username: credentials.username };
            } catch (error) {
                console.error('Login error:', error);
                throw new Error('Login failed');
            }
        },
        async register(userData) {
            try {
                await axios.post('/api/register/', userData);
            } catch (error) {
                console.error('Registration error:', error.response?.data || error.message);
                throw new Error('Registration failed');
            }
        },
        logout() {
            this.user = null;
            this.accessToken = null;
            this.refreshToken = null;

            localStorage.removeItem('accessToken');
            localStorage.removeItem('refreshToken');
        },
        async refreshToken() {
            try {
                const response = await axios.post('/api/token/refresh/', {
                    refresh: this.refreshToken,
                });
                this.accessToken = response.data.access;
                localStorage.setItem('accessToken', this.accessToken);
            } catch (error) {
                this.logout();
            }
        },
    },
});