<template>
  <div class="container mx-auto p-4">
    <h1 class="text-2xl font-bold mb-4">Favorite Bookmarks</h1>

    <div v-if="loading" class="text-center">
      <p>Loading favorite bookmarks...</p>
    </div>

    <div v-else>
      <ul>
        <li v-for="bookmark in favoriteBookmarks" :key="bookmark.id" class="mb-2">
          <a :href="bookmark.url" target="_blank" class="text-blue-500">{{ bookmark.title }}</a>
        </li>
      </ul>
      <div v-if="favoriteBookmarks.length === 0">
        <p>No favorite bookmarks.</p>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue'
import api from '../services/api'

export default {
  setup() {
    const favoriteBookmarks = ref([])
    const loading = ref(true)

    const fetchFavorites = async () => {
      try {
        const response = await api.get('bookmarks/', {
          params: {
            is_favorite: true, // Assuming your API supports filtering
          },
        })
        favoriteBookmarks.value = response.data.filter(b => b.is_favorite)
      } catch (error) {
        console.error('Error fetching favorite bookmarks:', error)
      } finally {
        loading.value = false
      }
    }

    onMounted(() => {
      fetchFavorites()
    })

    return {
      favoriteBookmarks,
      loading,
    }
  },
}
</script>

<style scoped>

</style>
