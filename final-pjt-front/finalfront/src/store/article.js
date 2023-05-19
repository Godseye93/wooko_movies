import axios from 'axios';
import communityUrl from '@/api_url/communityUrl';

const movie = {
  state: {
    allArticles: [],
  },
  getters: {
    getAllArticles(state) {
      return state.allArticles;
    },
  },
  mutations: {
    SET_ALL_ARTICLES(state, allArticles) {
      state.allArticles = allArticles;
    },
  },
  actions: {
    // 게시글 생성
    createArticle(context, articleInfo) {
      axios({
        method: 'post',
        url: communityUrl.createArticle(),
        data: articleInfo,
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
    fetchAllArticles(context) {
      axios({
        method: 'get',
        url: communityUrl.getAllArticles(),
        headers: {
          Authorization: `Token ${context.rootState.auth.token}`,
        },
      })
        .then((res) => {
          context.commit('SET_ALL_ARTICLES', res.data);
        })
        .catch((err) => {
          alert(err);
        });
    },
  },
};

export default movie;
