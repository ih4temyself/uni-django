// src/store/index.js
import { defineStore } from 'pinia'
import api from '../services/api'

export const useBookmarkStore = defineStore('bookmarkStore', {
    state: () => ({
        bookmarks: [],
        categories: [],
        loading: false,
    }),
    actions: {
        async fetchBookmarks() {
            this.loading = true
            try {
                const response = await api.get('bookmarks/')
                this.bookmarks = response.data
            } catch (error) {
                console.error('Error fetching bookmarks:', error)
            } finally {
                this.loading = false
            }
        },
        async fetchCategories() {
            try {
                const response = await api.get('categories/')
                this.categories = response.data
            } catch (error) {
                console.error('Error fetching categories:', error)
            }
        },
        async deleteBookmark(id) {
            try {
                await api.delete(`bookmarks/${id}/`)
                this.bookmarks = this.bookmarks.filter(b => b.id !== id)
            } catch (error) {
                console.error('Error deleting bookmark:', error)
            }
        },
    },
})
