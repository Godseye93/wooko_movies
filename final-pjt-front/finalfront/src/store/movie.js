import axios from 'axios';
import movieUrl from '@/api_url/movieUrl';

const movie = {
  state: {
    recommendedMovies: [],
    highRatingMovies: [],
    latestMovies: [],
    movieDetail: {},
  },
  getters: {
    getRecommendedMovies(state) {
      return state.recommendedMovies;
    },
    getHighRatingMovies(state) {
      return state.highRatingMovies;
    },
    getLatestMovies(state) {
      return state.latestMovies;
    },
    getMovieDetail(state) {
      return state.movieDetail;
    },
  },
  mutations: {
    SET_RECOMMENDED_MOVIES(state, recommendedMovies) {
      state.recommendedMovies = recommendedMovies;
    },
    SET_HIGH_RATING_MOVIES(state, highRatingMovies) {
      state.highRatingMovies = highRatingMovies;
    },
    SET_LATEST_MOVIES(state, latestMovies) {
      state.latestMovies = latestMovies;
    },
    SET_MOVIE_DETAIL(state, movieDetail) {
      state.movieDetail = movieDetail;
    },
  },
  actions: {
    getSortedMovies({ commit }, sortMethod) {
      axios({
        method: 'get',
        url: movieUrl.sortedMovies(sortMethod),
      })
        .then((res) => {
          if (sortMethod === 'vote_average') {
            commit('SET_HIGH_RATING_MOVIES', res.data);
          } else if (sortMethod === 'release_date') {
            commit('SET_LATEST_MOVIES', res.data);
          } else {
            commit('SET_RECOMMENDED_MOVIES', res.data);
          }
        })
        .catch((err) => {
          alert(err);
        });
    },

    fetchMovieDetail({ commit }, movieId) {
      axios({
        method: 'get',
        url: movieUrl.detailMovies(movieId),
      })
        .then((res) => {
          commit('SET_MOVIE_DETAIL', res.data);
        })
        .catch((err) => {
          alert(err);
        });
    },
  },
};

export default movie;
