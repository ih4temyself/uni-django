<template>
  <div class="container mx-auto p-4">
    <div v-if="loading" class="text-center">
      <p>Loading bookmark...</p>
    </div>

    <div v-else-if="bookmark">
      <h1 class="text-2xl font-bold mb-4">{{ bookmark.title }}</h1>
      <p><strong>URL:</strong> <a :href="bookmark.url" target="_blank" class="text-blue-500">{{ bookmark.url }}</a></p>
      <p v-if="bookmark.category"><strong>Category:</strong> {{ bookmark.category.name }}</p>
      <p><strong>Favorite:</strong> {{ bookmark.is_favorite ? 'Yes' : 'No' }}</p>

      <div class="mt-4">
        <router-link :to="`/edit/${bookmark.id}`" class="btn btn-secondary">Edit</router-link>
        <button @click="deleteBookmark(bookmark.id)" class="btn btn-danger ml-2">Delete</button>
      </div>
    </div>

    <div v-else>
      <p>Bookmark not found.</p>
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import api from '../services/api'

export default {
  setup() {
    const route = useRoute()
    const router = useRouter()
    const bookmark = ref(null)
    const loading = ref(true)

    const fetchBookmark = async () => {
      try {
        const response = await api.get(`bookmarks/${route.params.id}/`)
        bookmark.value = response.data
      } catch (error) {
        if (error.response && error.response.status === 404) {
          router.replace('/not-found')
        } else {
          console.error('Error fetching bookmark:', error)
        }
      } finally {
        loading.value = false
      }
    }

    const deleteBookmark = async (id) => {
      if (confirm('Are you sure you want to delete this bookmark?')) {
        try {
          await api.delete(`bookmarks/${id}/`)
          router.push('/')
        } catch (error) {
          console.error('Error deleting bookmark:', error)
        }
      }
    }

    onMounted(() => {
      fetchBookmark()
    })

    return {
      bookmark,
      loading,
      deleteBookmark,
    }
  },
}
</script>

<style scoped>
.btn {
  @apply px-4 py-2 bg-gray-500 text-white rounded;
}
.btn-secondary {
  @apply hover:bg-gray-600;
}
.btn-danger {
  @apply bg-red-500 hover:bg-red-600;
}
</style>
