<template>
  <div class="container mx-auto p-4">
    <div class="flex justify-between items-center mb-4">
      <h1 class="text-2xl font-bold">Bookmarks</h1>
      <router-link to="/add" class="bg-gray-700 hover:text-gray-800 font-semibold py-2 px-4 border border-gray-400 rounded shadow">Add Bookmark</router-link>
    </div>

    <CategoryFilter @filter="filterByCategory" />

    <div v-if="loading" class="text-center">
      <p>Loading bookmarks...</p>
    </div>

    <div v-else>
      <div v-if="filteredBookmarks.length">
        <ul>
          <li
              v-for="bookmark in filteredBookmarks"
              :key="bookmark.id"
              class="mb-3 flex justify-between items-center p-4 border rounded hover:bg-gray-700 cursor-pointer"
              @click="navigateToBookmark(bookmark.id)"
          >
            <div class="flex items-center" @click.stop>
                <span v-if="bookmark.is_favorite" class="mr-4">
                  <svg xmlns="http://www.w3.org/2000/svg" fill="currentColor" class="h-6 w-6 text-yellow-500" viewBox="0 0 24 24">
                    <path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/>
                  </svg>
                </span>

              <div>
                <a
                    :href="bookmark.url"
                    target="_blank"
                    rel="noopener noreferrer"
                    class="text-black-500 hover:underline font-semibold"
                    @click.stop
                >
                  {{ bookmark.title }}
                </a>
                <p class="text-sm text-gray-400">
                  Category:
                  <span v-if="bookmark.category" class="category-label">{{ bookmark.category.name }}</span>
                  <span v-else>No Category</span>
                </p>
              </div>
            </div>

            <div class="flex items-center" @click.stop>
              <router-link
                  :to="`/edit/${bookmark.id}`"
                  class="text-sm text-gray-600 hover:text-gray-800 mr-2"
              >
                Edit
              </router-link>
              <button
                  @click="deleteBookmark(bookmark.id)"
                  class="text-sm text-red-600 hover:text-red-800"
              >
                Delete
              </button>
            </div>
          </li>
        </ul>
      </div>
      <div v-else>
        <p>No bookmarks available.</p>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, onMounted, computed } from 'vue'
import { useRouter } from 'vue-router'
import { useBookmarkStore } from '../store'
import CategoryFilter from './CategoryFilter.vue'

export default {
  components: { CategoryFilter },
  setup() {
    const router = useRouter()
    const store = useBookmarkStore()

    const loading = computed(() => store.loading)
    const bookmarks = computed(() => store.bookmarks)
    const categories = computed(() => store.categories)
    const selectedCategory = ref(null)

    onMounted(() => {
      store.fetchCategories()
      store.fetchBookmarks()
    })

    const deleteBookmark = async (id) => {
      if (confirm('Are you sure you want to delete this bookmark?')) {
        await store.deleteBookmark(id)
      }
    }

    const filterByCategory = (categoryId) => {
      selectedCategory.value = categoryId
    }

    const filteredBookmarks = computed(() => {
      if (selectedCategory.value) {
        return bookmarks.value.filter(
            (b) => b.category && b.category.id === selectedCategory.value
        )
      }
      return bookmarks.value
    })

    const navigateToBookmark = (id) => {
      router.push(`/bookmarks/${id}`)
    }

    return {
      loading,
      bookmarks,
      categories,
      selectedCategory,
      deleteBookmark,
      filterByCategory,
      filteredBookmarks,
      navigateToBookmark,
    }
  },
}
</script>

<style scoped>
.category-label {
  background-color: lightgreen;
  padding: 4px 8px;
}
.btn {
  @apply px-4 py-2 bg-transparent  text-white rounded;
}
.btn-primary {
  @apply hover:bg-blue-600;
}
.btn-secondary {
  @apply bg-gray-500 hover:bg-gray-600 text-white;
}
</style>