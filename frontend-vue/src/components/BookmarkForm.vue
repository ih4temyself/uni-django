<!-- src/components/BookmarkForm.vue -->
<template>
  <div class="container mx-auto p-4">
    <h1 class="text-2xl font-bold mb-4">{{ isEdit ? 'Edit Bookmark' : 'Add Bookmark' }}</h1>

    <form @submit.prevent="handleSubmit">
      <div class="mb-4">
        <label class="block mb-1" for="title">Title</label>
        <input
            v-model="form.title"
            id="title"
            type="text"
            required
            class="w-full px-3 py-2 border rounded"
            style="background-color: #387478"
        />
      </div>

      <div class="mb-4">
        <label class="block mb-1" for="url">URL</label>
        <input
            v-model="form.url"
            id="url"
            type="url"
            required
            class="w-full px-3 py-2 border rounded"
            style="background-color: #387478"
        />
      </div>

      <div class="mb-4">
        <label class="block mb-1" for="category">Category</label>
        <select v-model="form.category_id" id="category" class="w-full border rounded bg-black">
          <option value="">No Category</option>
          <option v-for="category in categories" :key="category.id" :value="category.id">{{ category.name }}</option>
        </select>
      </div>

      <div class="mb-4">
        <label class="inline-flex items-center">
          <input type="checkbox" v-model="form.is_favorite" class="form-checkbox" />
          <span class="ml-2" style="background-color: #387478">Mark as Favorite</span>
        </label>
      </div>

      <div class="mb-4">
        <label class="block mb-1" for="newCategory">Or Add New Category</label>
        <input
            v-model="form.new_category"
            id="newCategory"
            type="text"
            placeholder="New Category Name"
            class="w-full px-3 py-2 border rounded"
            style="background-color: #387478"
        />
      </div>

      <div>
        <button type="submit" class="btn btn-primary">{{ isEdit ? 'Update' : 'Add' }}</button>
        <router-link to="/" class="btn btn-secondary ml-2">Cancel</router-link>
      </div>
    </form>
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
    const isEdit = ref(false)
    const form = ref({
      title: '',
      url: '',
      category_id: '',
      is_favorite: false,
      new_category: '',
    })
    const categories = ref([])

    const fetchCategories = async () => {
      try {
        const response = await api.get('categories/')
        categories.value = response.data
      } catch (error) {
        console.error('Error fetching categories:', error)
      }
    }

    const fetchBookmark = async () => {
      if (route.params.id) {
        isEdit.value = true
        try {
          const response = await api.get(`bookmarks/${route.params.id}/`)
          form.value.title = response.data.title
          form.value.url = response.data.url
          form.value.category_id = response.data.category_id
          form.value.is_favorite = response.data.is_favorite
        } catch (error) {
          if (error.response && error.response.status === 404) {
            router.replace('/not-found')
          } else {
            console.error('Error fetching bookmark:', error)
          }
        }
      }
    }

    const handleSubmit = async () => {
      const payload = {
        title: form.value.title,
        url: form.value.url,
        is_favorite: form.value.is_favorite,
      }

      if (form.value.new_category.trim()) {
        payload.category_name = form.value.new_category.trim()
      } else if (form.value.category_id) {
        payload.category_id = form.value.category_id
      }

      try {
        if (isEdit.value) {
          await api.put(`bookmarks/${route.params.id}/`, payload)
          router.push(`/bookmarks/${route.params.id}`)
        } else {
          await api.post('bookmarks/', payload)
          router.push('/')
        }
      } catch (error) {
        console.error('Error submitting form:', error)
      }
    }

    onMounted(() => {
      fetchCategories()
      fetchBookmark()
    })

    return {
      isEdit,
      form,
      categories,
      handleSubmit,
    }
  },
}
</script>

<style scoped>
.btn {
  @apply px-4 py-2 text-white rounded;
}
.btn-primary {
  @apply hover:bg-green-900;
}
.btn-secondary {
  @apply bg-gray-500 hover:bg-gray-600 text-white;
}
</style>
