import axios from 'axios';
import movieUrl from '@/api_url/movieUrl';

const movie = {
  state: {
    recommendedMovies: [],
    highRatingMovies: [],
    latestMovies: [],
    searchMovies: [],
    movieDetail: {},
    contestants: [],
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
    getSearchedMovies(state) {
      return state.searchMovies;
    },
    getContestants(state) {
      return state.contestants;
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
    SET_SEARCHED_MOVIES(state, searchMovies) {
      state.searchMovies = searchMovies;
    },
    SET_CONTESTANTS(state, contestants) {
      state.contestants = contestants;
    },
  },
  actions: {
    getSortedMovies({ commit }, sortMethod) {
      let url = '';
      if (sortMethod === 'vote_average') {
        url = movieUrl.highRatingMovies();
      } else if (sortMethod === 'release_date') {
        url = movieUrl.latestMovies();
      } else {
        url = movieUrl.recommendedMovies();
      }
      axios({
        method: 'get',
        url,
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
    fetchSearchMovies({ commit }, keyword) {
      axios({
        method: 'get',
        url: movieUrl.searchMovies(keyword),
      })
        .then((res) => {
          commit('SET_SEARCHED_MOVIES', res.data.movies);
        })

        .catch((err) => {
          alert(err);
        });
    },
    getRandContestants({ commit }, count) {
      axios({
        method: 'get',
        url: movieUrl.randContestants(count),
      })
        .then((res) => {
          commit('SET_CONTESTANTS', res.data);
        })
        .catch((err) => {
          alert(err);
        });
    },
    sendGameResult(context, result) {
      axios({
        method: 'post',
        url: movieUrl.addLikeGenre(),
        data: result,
        headers: {
          Authorization: `Token ${context.rootState.auth.token}`,
        },
      })
        .then((res) => {
          console.log(res);
        })
        .catch((err) => {
          alert(err);
        });
    },
  },
};

export default movie;
