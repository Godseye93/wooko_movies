const MOVIES_HOST = 'http://127.0.0.1:8000/movies/';

export default {
  // 메인 페이지 추천순, 평점순, 최신순 영화 조회
  sortedMovies: (sortMethod) =>
    MOVIES_HOST + `recommended/?sort_by=${sortMethod}/`,

  // // 영화 상세 조회(데이터 출력용)
  detailMovies: (movieId) => MOVIES_HOST + `${movieId}/`,
  // // 영화별 리뷰 게시글 조회
  searchMovies: (keyword) => MOVIES_HOST + `?search=${keyword}`,
  // searchMovies: () => 'http://127.0.0.1:8000/movies/?search=더',
  // // 추천 영화 조회
  // movie_recommend: (genre_id) => MOVIES_HOST + `${genre_id}/genre/`,
};
