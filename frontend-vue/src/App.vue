<!-- src/App.vue -->
<template>
  <div id="app">
    <nav>
      <span v-if="isLoggedIn && user">Hello, {{ user.username }} </span>
      <router-link v-if="!isLoggedIn" to="/login">Login </router-link>
      <router-link v-if="!isLoggedIn" to="/register">Register</router-link>
      <button v-if="isLoggedIn" @click="logoutUser"> Logout</button>
    </nav>
    <router-view />
  </div>
</template>

<script>
import { useAuthStore } from './store/authStore';

export default {
  computed: {
    isLoggedIn() {
      const authStore = useAuthStore();
      return !!authStore.accessToken; // Check if there's an access token
    },
    user() {
      const authStore = useAuthStore();
      return authStore.user; // Access the `user` state from the store
    },
  },
  methods: {
    logoutUser() {
      const authStore = useAuthStore();
      authStore.logout();
      this.$router.push('/login');
    },
  },
};
</script>
