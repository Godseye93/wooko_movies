const AUTH_HOST = 'http://127.0.0.1:8000/api/auth/';
const USER_HOST = 'http://127.0.0.1:8000/user/';

export default {
  //   // 로그인
  login: () => AUTH_HOST + 'login/',
  //   // 로그아웃
  logout: () => AUTH_HOST + 'logout/',
  // 회원가입
  signup: () => AUTH_HOST + 'signup/',
  //   // 현재 user 정보(Token으로 판별) =>
  currentUserInfo: () => AUTH_HOST + `user/`,
  //   // 비밀번호 변경
  //   changepassword: () => HOST + 'account/' + 'password/change/',
  //   // 회원탈퇴
  delUser: () => USER_HOST,
  //   // 프로필 조회
  profileDetail: (userId) => USER_HOST + `${userId}/profile/`,
  //   // 프로필 수정
  profileUpdate: () => USER_HOST + `profile/`,

  changePasswd: () => AUTH_HOST + `password/change/`,

  followToggle: (userId) => USER_HOST + `${userId}/follow/`,
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
