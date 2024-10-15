import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';

Vue.use(Vuex);

export default new Vuex.Store({
    state: {
        user: null,
        accessToken: localStorage.getItem('accessToken') || null,
        refreshToken: localStorage.getItem('refreshToken') || null,
    },
    mutations: {
        setUser(state, user) {
            state.user = user;
        },
        setTokens(state, { access, refresh }) {
            state.accessToken = access;
            state.refreshToken = refresh;
            localStorage.setItem('accessToken', access);
            localStorage.setItem('refreshToken', refresh);
        },
        clearTokens(state) {
            state.accessToken = null;
            state.refreshToken = null;
            localStorage.removeItem('accessToken');
            localStorage.removeItem('refreshToken');
        },
    },
    actions: {
        async login({ commit }, credentials) {
            const response = await axios.post('/api/token/', credentials);
            commit('setTokens', response.data);
            // Optionally fetch user info here
            const userResponse = await axios.get('/api/user-info/', {
                headers: { Authorization: `Bearer ${response.data.access}` },
            });
            commit('setUser', userResponse.data);
        },
        logout({ commit }) {
            commit('clearTokens');
            commit('setUser', null);
        },
        async refreshToken({ state, commit }) {
            const response = await axios.post('/api/token/refresh/', { refresh: state.refreshToken });
            commit('setTokens', { access: response.data.access, refresh: state.refreshToken });
        },
    },
});
