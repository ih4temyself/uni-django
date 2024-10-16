// src/store/bookmarkStore.js
import { defineStore } from 'pinia';
import axios from 'axios';

export const useBookmarkStore = defineStore('bookmark', {
    state: () => ({
        bookmarks: [],
        categories: [],
        loading: false,
    }),
    actions: {
        async fetchBookmarks() {
            this.loading = true;
            try {
                const response = await axios.get('/api/bookmarks/');
                this.bookmarks = response.data;
            } catch (error) {
                console.error('Failed to fetch bookmarks:', error);
            } finally {
                this.loading = false;
            }
        },
        async fetchCategories() {
            try {
                const response = await axios.get('/api/categories/');
                this.categories = response.data;
            } catch (error) {
                console.error('Failed to fetch categories:', error);
            }
        },
        async deleteBookmark(id) {
            try {
                await axios.delete(`/api/bookmarks/${id}/`);
                this.fetchBookmarks();
            } catch (error) {
                console.error('Failed to delete bookmark:', error);
            }
        },
    },
});
