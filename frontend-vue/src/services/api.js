import axios from 'axios'
import { useAuthStore } from '../store/authStore'

const api = axios.create({
    baseURL: 'http://localhost:8000/api/',
    headers: {
        'Content-Type': 'application/json',
    },
})

api.interceptors.request.use((config) => {
    const authStore = useAuthStore()
    const token = authStore.accessToken
    if (token) {
        config.headers.Authorization = `Bearer ${token}`
    }
    return config
})

export default api
