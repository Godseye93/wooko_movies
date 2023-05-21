import axios from 'axios';
import accountsUrl from '@/api_url/accountsUrl';
import router from '@/router';

const auth = {
  state: {
    token: null,
    curUser: {},
    profileInfo: {},
  },

  getters: {
    isLogin(state) {
      return state.token ? true : false;
    },
    getCurUser(state) {
      return state.curUser;
    },
    getProfileInfo(state) {
      return state.profileInfo;
    },
  },

  mutations: {
    SAVE_TOKEN(state, token) {
      state.token = token;
    },
    SET_CUR_USER(state, curUser) {
      state.curUser = curUser;
    },
    SET_PROFILE_INFO(state, profileInfo) {
      state.profileInfo = profileInfo;
    },
  },

  actions: {
    fetchSignUp(context, userInfo) {
      axios({
        method: 'post',
        url: accountsUrl.signup(),
        data: userInfo,
      })
        .then((res) => {
          context.commit('SAVE_TOKEN', res.data.key);
          context.dispatch('fetchCurUserInfo');
          router.push({ name: 'home' }); // 홈으로 이동
        })
        .catch((err) => {
          alert(err);
        });
    },
    fetchLogin(context, loginInfo) {
      axios({
        method: 'post',
        url: accountsUrl.login(),
        data: loginInfo,
      })
        .then((res) => {
          context.commit('SAVE_TOKEN', res.data.key);
          context.dispatch('fetchCurUserInfo');
          router.push({ name: 'home' }); // 홈으로 이동
        })
        .catch((err) => {
          alert(err);
        });
    },
    fetchLogout(context) {
      axios({
        method: 'post',
        url: accountsUrl.logout(),
        headers: {
          Authorization: `Token ${context.state.token}`,
        },
      })
        .then(() => {
          context.commit('SAVE_TOKEN', null);
          context.commit('SET_CUR_USER', {});
          if (router.currentRoute.name === 'home') return;
          router.push({ name: 'home' }); // 홈으로 이동
        })
        .catch((err) => {
          alert(err);
        });
    },
    fetchCurUserInfo(context) {
      axios({
        method: 'get',
        url: accountsUrl.currentUserInfo(),
        headers: {
          Authorization: `Token ${context.state.token}`,
        },
      })
        .then((res) => {
          context.commit('SET_CUR_USER', res.data);
        })
        .catch((err) => {
          alert(err);
        });
    },
    fetchProfileDetail(context, userId) {
      axios({
        method: 'get',
        url: accountsUrl.profileDetail(userId),
        headers: {
          Authorization: `Token ${context.state.token}`,
        },
      })
        .then((res) => {
          context.commit('SET_PROFILE_INFO', res.data);
        })
        .catch((err) => {
          alert(err);
        });
    },
    updateProfile(context, profileInfo) {
      axios({
        method: 'put',
        url: accountsUrl.profileUpdate(),
        data: profileInfo,
        headers: {
          Authorization: `Token ${context.state.token}`,
        },
      })
        .then((res) => {
          context.commit('SET_PROFILE_INFO', res.data);
          router.push({
            name: 'profile',
            params: { userId: context.state.curUser.pk },
          });
        })
        .catch((err) => {
          alert(err);
        });
    },
    fetchChangePasswd(context, passwdInfo) {
      axios({
        method: 'post',
        url: accountsUrl.changePasswd(),
        data: passwdInfo,
        headers: {
          Authorization: `Token ${context.state.token}`,
        },
      })
        .then(() => {
          router.push({
            name: 'profile',
            params: { userId: context.state.curUser.pk },
          });
        })
        .catch((err) => {
          alert(err);
        });
    },
    delUser(context) {
      axios({
        method: 'delete',
        url: accountsUrl.delUser(),
        headers: {
          Authorization: `Token ${context.state.token}`,
        },
      })
        .then((res) => {
          console.log(res);
          context.commit('SAVE_TOKEN', null);
          context.commit('SET_CUR_USER', {});
          router.push({ name: 'home' }); // 홈으로 이동
        })
        .catch((err) => {
          alert(err);
        });
    },
  },
};
export default auth;
