const AUTH_HOST = 'http://127.0.0.1:8000/api/auth/';

export default {
  //   // 로그인
  login: () => AUTH_HOST + 'login/',
  //   // 로그아웃
  //   logout: () => HOST + 'account/' + 'logout/',
  // 회원가입
  signup: () => AUTH_HOST + 'signup/',
  //   // 현재 user 정보(Token으로 판별) =>
  //   currentUserInfo: () => HOST + 'account/' + 'user/',
  //   // 비밀번호 변경
  //   changepassword: () => HOST + 'account/' + 'password/change/',
  //   // 회원탈퇴
  //   deletemember: () => HOST + ACCOUNTS + 'delete/',
  //   // 프로필 조회
  //   profile: (userId) => HOST + ACCOUNTS + `${userId}/profile/`,
  //   // 사용자의 영화 리스트 조회
  //   personalmovielist: (userId) => HOST + ACCOUNTS + `${userId}/list/`,
  //   // 사용자의 싫어요 장르 조회
  //   personalhatemovie: (userId) => HOST + ACCOUNTS + `${userId}/hate_genre/`,
  //   // 사용자의 싫어요 장르 등록 및 해제
  //   personalhatemovieupdate: (userId, genreId) =>
  //     HOST + ACCOUNTS + `${userId}/hate_genre/${genreId}/`,
  //   // 팔로우 등록 및 해제
  //   personalfollow: (userId) => HOST + ACCOUNTS + `${userId}/follow/`,
  //   // 친구 추천
  //   friendreco: (userId) => HOST + ACCOUNTS + `${userId}/friend/`,
  //   // 좋아요 기반 영화 추천
  //   recolike: (userId) => HOST + ACCOUNTS + `${userId}/reco_like/`,
  //   // 평점 기반 영화 추천
  //   recorate: (userId) => HOST + ACCOUNTS + `${userId}/reco_rate/`,
  // },
  // // 영화(메인페이지, movies) 관련 경로
  // // 영화 생성/수정/삭제 데이터 제작 필요
};
