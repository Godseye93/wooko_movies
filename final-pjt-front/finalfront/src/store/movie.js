import axios from 'axios';
import movieUrl from '@/api_url/movieUrl';
import router from '@/router';

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
    fetchRecommendedMovies(context, sortMethod) {
      let url = '';
      if (sortMethod === 'genre_recommend') {
        url = movieUrl.genreRecommend();
      } else if (sortMethod === 'actor_recommend') {
        url = movieUrl.actorRecommend();
      } else if (sortMethod === 'director_recommend') {
        url = movieUrl.directorRecommend();
      }

      axios({
        method: 'get',
        url,
        headers: {
          Authorization: `Token ${context.rootState.auth.token}`,
        },
      })
        .then((res) => {
          if (res.data === '검색 결과가 없습니다.') {
            context.dispatch('getSortedMovies', 'popularity');
          }
          context.commit('SET_RECOMMENDED_MOVIES', res.data);
        })
        .catch((err) => {
          alert(err);
        });
    },

    getSortedMovies(context, sortMethod) {
      let url = '';
      if (sortMethod === 'vote_average') {
        url = movieUrl.highRatingMovies();
      } else if (sortMethod === 'release_date') {
        url = movieUrl.latestMovies();
      } else if (sortMethod === 'popularity') {
        url = movieUrl.popularMovies();
      }
      axios({
        method: 'get',
        url,
      })
        .then((res) => {
          if (sortMethod === 'vote_average') {
            context.commit('SET_HIGH_RATING_MOVIES', res.data);
          } else if (sortMethod === 'release_date') {
            context.commit('SET_LATEST_MOVIES', res.data);
          } else {
            context.commit('SET_RECOMMENDED_MOVIES', res.data);
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
      let url = '';
      if (router.currentRoute.name === 'versus-game-movie') {
        url = movieUrl.addLikeGenre();
      }
      if (router.currentRoute.name === 'versus-game-director') {
        url = movieUrl.addLikeDirector();
      }
      if (router.currentRoute.name === 'versus-game-actor') {
        url = movieUrl.addLikeActor();
      }
      if (router.currentRoute.name === 'worldcup') {
        url = movieUrl.addLikeGenre();
      }
      axios({
        method: 'post',
        url,
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
    getRandDirectors({ commit }, count) {
      axios({
        method: 'get',
        url: movieUrl.randDirectors(count),
      })
        .then((res) => {
          commit('SET_CONTESTANTS', res.data);
        })
        .catch((err) => {
          alert(err);
        });
    },
    getRandActors({ commit }, count) {
      axios({
        method: 'get',
        url: movieUrl.randActors(count),
      })
        .then((res) => {
          commit('SET_CONTESTANTS', res.data);
        })
        .catch((err) => {
          alert(err);
        });
    },
  },
};

export default movie;
