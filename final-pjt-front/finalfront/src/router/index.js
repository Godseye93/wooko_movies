import Vue from 'vue';
import VueRouter from 'vue-router';
import HomeView from '../views/HomeView.vue';
import MovieDetailView from '../views/MovieDetailView.vue';
import LoginView from '../views/LoginView.vue';
import SearchView from '../views/SearchView.vue';
import CommunityView from '../views/CommunityView.vue';
import ArticleDetailView from '../views/ArticleDetailView.vue';
import ArticleCreateView from '../views/ArticleCreateView.vue';
import profileView from '../views/ProfileView.vue';
import ProfileUpdateView from '../views/ProfileUpdateView.vue';
import SignupView from '../views/SignupView.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView,
  },
  {
    path: '/detail/:movieId',
    name: 'movie-detail',
    component: MovieDetailView,
  },
  {
    path: '/movie/search/:keyword',
    name: 'movie-search',
    component: SearchView,
  },
  {
    path: '/community',
    name: 'community',
    component: CommunityView,
  },

  {
    path: '/community/article/:articleId',
    name: 'article-detail',
    component: ArticleDetailView,
  },
  {
    path: '/community/article/create',
    name: 'article-create',
    component: ArticleCreateView,
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignupView,
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView,
  },
  {
    path: '/profile',
    name: 'profile',
    component: profileView,
  },
  {
    path: '/profile/update',
    name: 'profile-update',
    component: ProfileUpdateView,
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
