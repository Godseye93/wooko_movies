const MOVIES_HOST = 'http://127.0.0.1:8000/movies/';

export default {
  // 메인 페이지 평점순
  highRatingMovies: () => MOVIES_HOST + 'recommended/?sort_by=vote_average',

  // 메인 페이지 최신순
  latestMovies: () => MOVIES_HOST + 'recommended/?sort_by=release_date',

  // 메인 페이지 인기순
  popularMovies: () => MOVIES_HOST + 'recommended/?sort_by=popularity',

  // // 영화 상세 조회(데이터 출력용)
  detailMovies: (movieId) => MOVIES_HOST + `${movieId}/`,
  // // 영화별 리뷰 게시글 조회
  searchMovies: (keyword) => MOVIES_HOST + `?search=${keyword}`,
  // searchMovies: () => 'http://127.0.0.1:8000/movies/?search=더',
  // // 추천 영화 조회
  // movie_recommend: (genre_id) => MOVIES_HOST + `${genre_id}/genre/`,
  randContestants: (count) => MOVIES_HOST + 'random/' + `?count=${count}`,
  addLikeGenre: () => MOVIES_HOST + 'get_liked_genres/',
  addLikeActor: () => MOVIES_HOST + 'get_liked_actor/',
  addLikeDirector: () => MOVIES_HOST + 'get_liked_director/',
  randDirectors: (count) =>
    MOVIES_HOST + 'random_director/' + `?count=${count}`,
  randActors: (count) => MOVIES_HOST + 'random_actor/' + `?count=${count}`,

  // 장르기반 영화추천
  genreRecommend: () => MOVIES_HOST + 'random-by-genre/',
  // 배우기반 영화추천
  actorRecommend: () => MOVIES_HOST + 'random-by-actor/',
  // 감독기반 영화추천
  directorRecommend: () => MOVIES_HOST + 'random-by-director/',
  getMoviesByGenres: (genreId) =>
    MOVIES_HOST + `recommended/?sort_by=vote_average&genre_id=${genreId}`,
  mainRandomMovies: () => MOVIES_HOST + 'mainrandom/',
};
