import axios from 'axios';
import accountsUrl from '@/api_url/accountsUrl';
import router from '@/router';

const auth = {
  state: {
    token: null,
  },

  getters: {
    isLogin(state) {
      return state.token ? true : false;
    },
  },

  mutations: {
    SAVE_TOKEN(state, token) {
      state.token = token;
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
          if (router.currentRoute.name === 'home') return;
          router.push({ name: 'home' }); // 홈으로 이동
        })
        .catch((err) => {
          alert(err);
        });
    },
  },
};
export default auth;
