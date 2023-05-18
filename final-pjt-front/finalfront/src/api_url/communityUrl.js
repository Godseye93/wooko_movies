// // 커뮤니티(리뷰/댓글, community) 관련 경로
// community: {
//   // 전체 review 조회 / 생성(영화를 선택하지 않은 review)
//   reviews: () => HOST + REVIEWS,
//   // 영화를 선택한 review 생성
//   movie_review: (movieId) => HOST + REVIEWS + `${movieId}/review/`,
//   // 필터링된 게시글 정보(최신순, 좋아요, 댓글 많은 순)
//   reviews_sort: (sort_num) => HOST + REVIEWS + `${sort_num}/sort/`,
//   // 단일 review 조회
//   review: (reviewId) => HOST + REVIEWS + `${reviewId}/`,
//   // review 좋아요
//   like_review: (reviewId) => HOST + REVIEWS + `${reviewId}/` + 'like/',
//   // 전체 comment 조회 및 생성(영화 선택 X)
//   comments: (reviewId) => HOST + REVIEWS + `${reviewId}/` + COMMENTS,
//   // 대댓글 생성 및 전체 댓글 수정 및 삭제
//   comment: (reviewId, superCommentId) =>
//     HOST + REVIEWS + `${reviewId}/` + COMMENTS + `${superCommentId}/`,
//   // 댓글 좋아요 등록 및 해제
//   like_comment: (reviewId, commentId) =>
//     HOST + REVIEWS + `${reviewId}/` + 'like/' + `${commentId}/`,
//   // 댓글별 좋아요 개수 조회

//   // 게시판 A vs B 주제 생성(관리자)
//   question_create: () => HOST + REVIEWS + 'question/',
//   // 주제와 전체 응답 수 조회
//   question_fetch: (questId) => HOST + REVIEWS + `${questId}/question/`,
//   // 주제와 특정 응답 수 조회
//   question_vote: (questId, voteId) =>
//     HOST + REVIEWS + `${questId}/vote/${voteId}/`,
//   // 투표(의견) 등록
//   question_like: (questId) => HOST + REVIEWS + `${questId}/vote/like/`,
// },
