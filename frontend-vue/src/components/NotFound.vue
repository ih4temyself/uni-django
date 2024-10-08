<template>
  <div class="container mx-auto p-4 text-center">
    <h1 class="text-4xl font-bold mb-4">404 - Not Found</h1>
    <p class="mb-4">The page you are looking for does not exist.</p>
    <router-link to="/" class="btn btn-primary">Go Home</router-link>
  </div>
</template>

<script>
export default {
  name: 'NotFound',
}
</script>

<style scoped>
.btn {
  @apply px-4 py-2 bg-blue-500 text-white rounded;
}
.btn-primary {
  @apply hover:bg-blue-600;
}
</style>
