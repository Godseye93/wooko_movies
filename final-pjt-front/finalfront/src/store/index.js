import Vue from 'vue';
import Vuex from 'vuex';
import movie from './movie';
import auth from './auth';
import article from './article';
import createPersistedState from 'vuex-persistedstate';

Vue.use(Vuex);

export default new Vuex.Store({
  plugins: [
    createPersistedState({
      paths: ['auth.token', 'auth.curUser'], // 토큰 상태만 로컬 스토리지에 저장
    }),
  ], // 플러그인 전역 설정
  state: {},
  getters: {},
  mutations: {},
  actions: {},
  modules: {
    movie,
    auth,
    article,
  },
});
