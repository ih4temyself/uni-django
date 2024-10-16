<template>
  <div class="login">
    <h2>Login</h2>
    <form @submit.prevent="submitForm">
      <div>
        <input v-model="username" placeholder="Username" required />
      </div>
      <div>
        <input v-model="password" placeholder="Password" type="password" required />
      </div>
      <div>
        <button type="submit">submit</button>
      </div>
    </form>
  </div>
</template>

<script>
import { useAuthStore } from '../store/authStore';

export default {
  data() {
    return {
      username: '',
      password: '',
    };
  },
  methods: {
    async submitForm() {
      const authStore = useAuthStore();
      try {
        await authStore.login({username: this.username, password: this.password});
        this.$router.push('/');
      } catch (error) {
        alert('Login failed');
      }
    },
  },
};
</script>

<style scoped>
.login {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  flex-direction: column;
}

form {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

input {
  color: black;
  padding: 10px;
  font-size: 16px;
  width: 250px;
}

button {
  padding: 10px;
  font-size: 16px;
  cursor: pointer;
}
</style>
