<template>
    <div>
      <h2>Add Bookmark</h2>
      <form @submit.prevent="addBookmark">
        <div>
          <label for="url">URL:</label>
          <input v-model="url" type="text" id="url" required />
        </div>
        <div>
          <label for="title">Title:</label>
          <input v-model="title" type="text" id="title" required />
        </div>
        <div>
          <label for="category_name">Category Name:</label>
          <input
            v-model="category_name"
            type="text"
            id="category_name"
            placeholder="Enter new category"
          />
        </div>
        <div>
          <label for="category_id">Select Existing Category:</label>
          <select v-model="category_id" id="category_id">
            <option value="">None</option>
            <option
              v-for="category in categories"
              :key="category.id"
              :value="category.id"
            >
              {{ category.name }}
            </option>
          </select>
        </div>
        <button type="submit">Add Bookmark</button>
      </form>
    </div>
  </template>
  
  <script>
import axios from 'axios';

export default {
  data() {
    return {
      url: '',
      title: '',
      category_name: '',
      category_id: '',
      categories: [],
    };
  },
  methods: {
    fetchCategories() {
      axios
        .get('categories/')
        .then(response => {
          this.categories = response.data;
        })
        .catch(error => {
          console.error('Error fetching categories:', error);
        });
    },
    addBookmark() {
        const data = {
            url: this.url,
            title: this.title,
            is_favorite: false,
        };

        if (this.category_name) {
            data.category_name = this.category_name;
        } else if (this.category_id) {
            data.category_id = this.category_id;
        }

        console.log('Bookmark data being sent:', data);

        axios
            .post('bookmarks/', data)
            .then(() => {
                this.url = '';
                this.title = '';
                this.category_name = '';
                this.category_id = '';
                this.$emit('bookmark-added');
            })
            .catch(error => {
                console.error('Error adding bookmark:', error);
            });
    },


  },
  created() {
    this.fetchCategories();
  },
};
</script>
