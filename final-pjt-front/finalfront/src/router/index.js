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
import ArticleUpdateView from '../views/ArticleUpdateView.vue';
import ChangePasswdView from '../views/ChangePasswdView.vue';
import VersusGameMovieView from '../views/VersusGameMovieView.vue';
import WorldcupView from '../views/WorldcupView.vue';
import VersusGameActorView from '../views/VersusGameActorView.vue';
import VersusGameDirectorView from '../views/VersusGameDirectorView.vue';

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
    path: '/community/article/update/:articleId',
    name: 'article-update',
    component: ArticleUpdateView,
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
    path: '/profile/:userId',
    name: 'profile',
    component: profileView,
  },
  {
    path: '/profile/update',
    name: 'profile-update',
    component: ProfileUpdateView,
  },
  {
    path: '/changepasswd',
    name: 'change-passwd',
    component: ChangePasswdView,
  },
  {
    path: '/versusgame/movie',
    name: 'versus-game-movie',
    component: VersusGameMovieView,
  },
  {
    path: '/worldcup/:round',
    name: 'worldcup',
    component: WorldcupView,
  },
  {
    path: 'versusgame/actor',
    name: 'versus-game-actor',
    component: VersusGameActorView,
  },
  {
    path: 'versusgame/director',
    name: 'versus-game-director',
    component: VersusGameDirectorView,
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
