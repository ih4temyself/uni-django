import { createRouter, createWebHistory } from 'vue-router';
import BookmarkList from '../components/BookmarkList.vue';
import BookmarkDetail from '../components/BookmarkDetail.vue';
import BookmarkForm from '../components/BookmarkForm.vue';
import NotFound from '../components/NotFound.vue';
import Login from '../components/Login.vue';
import Register from '../components/Register.vue';
import { useAuthStore } from '../store/authStore';

const routes = [
    {
        path: '/',
        name: 'Home',
        component: BookmarkList,
        meta: { requiresAuth: true },
    },
    {
        path: '/bookmarks/:id',
        name: 'BookmarkDetail',
        component: BookmarkDetail,
        props: true,
        meta: { requiresAuth: true },
    },
    {
        path: '/add',
        name: 'AddBookmark',
        component: BookmarkForm,
        meta: { requiresAuth: true },
    },
    {
        path: '/edit/:id',
        name: 'EditBookmark',
        component: BookmarkForm,
        props: true,
        meta: { requiresAuth: true },
    },
    {
        path: '/login',
        name: 'Login',
        component: Login,
    },
    {
        path: '/register',
        name: 'Register',
        component: Register,
    },
    {
        path: '/:pathMatch(.*)*',
        name: 'NotFound',
        component: NotFound,
    },
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

router.beforeEach((to, from, next) => {
    const authStore = useAuthStore();
    if (to.matched.some(record => record.meta.requiresAuth) && !authStore.accessToken) {
        next('/login');
    } else if ((to.path === '/login' || to.path === '/register') && authStore.accessToken) {
        next('/');
    } else {
        next();
    }
});

export default router;
