// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router'
import BookmarkList from '../components/BookmarkList.vue'
import BookmarkDetail from '../components/BookmarkDetail.vue'
import BookmarkForm from '../components/BookmarkForm.vue'
import NotFound from '../components/NotFound.vue'

const routes = [
    {
        path: '/',
        name: 'Home',
        component: BookmarkList,
    },
    {
        path: '/bookmarks/:id',
        name: 'BookmarkDetail',
        component: BookmarkDetail,
        props: true,
    },
    {
        path: '/add',
        name: 'AddBookmark',
        component: BookmarkForm,
    },
    {
        path: '/edit/:id',
        name: 'EditBookmark',
        component: BookmarkForm,
        props: true,
    },
    {
        path: '/:pathMatch(.*)*',
        name: 'NotFound',
        component: NotFound,
    },
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

export default router
