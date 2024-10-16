<template>
  <div class="register">
    <h2>Register</h2>
    <form @submit.prevent="submitForm">
      <div>
        <input v-model="username" placeholder="Username" required />
      </div>
      <div>
        <input v-model="first_name" placeholder="First Name (optional)" />
      </div>
      <div>
        <input v-model="last_name" placeholder="Last Name (optional)" />
      </div>
      <div>
        <input v-model="email" placeholder="Email" required />
      </div>
      <div>
        <input v-model="password" placeholder="Password" type="password" required />
      </div>
      <div>
        <input v-model="password_check" placeholder="Confirm Password" type="password" required />
      </div>
      <div>
        <button type="submit">Register</button>
      </div>
    </form>
  </div>
</template>

<script>
import {useAuthStore} from '../store/authStore';

export default {
  data() {
    return {
      username: '',
      first_name: '',
      last_name: '',
      email: '',
      password: '',
      password_check: '',
    };
  },
  methods: {
    async submitForm() {
      if (this.password !== this.password_check) {
        alert('Passwords do not match');
        return;
      }

      const authStore = useAuthStore();
      try {
        const response = await authStore.register({
          username: this.username,
          first_name: this.first_name,
          last_name: this.last_name,
          email: this.email,
          password: this.password,
          password_check: this.password_check,
        });

        alert('User registered successfully! Please log in.');
        this.$router.push('/login');
      } catch (error) {
        console.error('Registration failed:', error);
        if (error.response && error.response.data) {
          alert(`Registration failed: ${JSON.stringify(error.response.data)}`);
        } else {
          alert('Registration failed: An unknown error occurred.');
        }
      }
    },
  },
};
</script>

<style scoped>
.register {
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
