<template>
    <div>
      <h1>Bookmarks</h1>
      <BookmarkForm @bookmark-added="fetchBookmarks" />
      <ul>
        <li v-for="bookmark in bookmarks" :key="bookmark.id">
          <a :href="bookmark.url" target="_blank">{{ bookmark.title }}</a>
          <span v-if="bookmark.category">
            (Category: {{ bookmark.category.name }})
          </span>
          <button @click="deleteBookmark(bookmark.id)">Delete</button>
          <button @click="toggleFavorite(bookmark)">
            {{ bookmark.is_favorite ? 'Unfavorite' : 'Favorite' }}
          </button>
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  import { ref, onMounted } from 'vue';
  import BookmarkForm from './BookmarkForm.vue';
  
  export default {
    name: 'BookmarkList',
    components: {
      BookmarkForm,
    },
    setup() {
      const bookmarks = ref([]);
  
      const fetchBookmarks = () => {
        axios
          .get('bookmarks/')
          .then((response) => {
            bookmarks.value = response.data;
          })
          .catch((error) => {
            console.error(error);
          });
      };
  
      const deleteBookmark = (id) => {
        axios
          .delete(`bookmarks/${id}/`)
          .then(() => {
            fetchBookmarks();
          })
          .catch((error) => {
            console.error(error);
          });
      };
  
      const toggleFavorite = (bookmark) => {
        axios
          .patch(`bookmarks/${bookmark.id}/`, {
            is_favorite: !bookmark.is_favorite,
          })
          .then(() => {
            fetchBookmarks();
          })
          .catch((error) => {
            console.error(error);
          });
      };
  
      onMounted(() => {
        fetchBookmarks();
      });
  
      return {
        bookmarks,
        fetchBookmarks,
        deleteBookmark,
        toggleFavorite,
      };
    },
  };
  </script>
  
  <style scoped>
  /* Add component-specific styles here */
  </style>