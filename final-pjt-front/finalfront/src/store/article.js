import axios from 'axios';
import communityUrl from '@/api_url/communityUrl';

const movie = {
  state: {},
  getters: {},
  mutations: {},
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
          alert('게시글이 생성되었습니다.', res);
        })
        .catch((err) => {
          alert(err);
        });
    },
  },
};

export default movie;
