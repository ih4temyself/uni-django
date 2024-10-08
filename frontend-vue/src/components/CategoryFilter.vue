<template>
  <div class="mb-4">
    <label class="block mb-1">Filter by Category:</label>
    <select v-model="selected" @change="emitFilter" class="w-full bg-black py-2 border rounded">
      <option value="">All Categories</option>
      <option v-for="category in categories" :key="category.id" :value="category.id">{{ category.name }}</option>
    </select>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue'
import api from '../services/api'

export default {
  emits: ['filter'],
  setup(props, { emit }) {
    const categories = ref([])
    const selected = ref('')

    const fetchCategories = async () => {
      try {
        const response = await api.get('categories/')
        categories.value = response.data
      } catch (error) {
        console.error('Error fetching categories:', error)
      }
    }

    const emitFilter = () => {
      emit('filter', selected.value)
    }

    onMounted(() => {
      fetchCategories()
    })

    return {
      categories,
      selected,
      emitFilter,
    }
  },
}
</script>

<style scoped>
</style>
