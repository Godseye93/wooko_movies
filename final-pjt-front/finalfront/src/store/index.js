import Vue from 'vue';
import Vuex from 'vuex';
import movie from './movie';
import auth from './auth';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {},
  getters: {},
  mutations: {},
  actions: {},
  modules: {
    movie,
    auth,
  },
});
