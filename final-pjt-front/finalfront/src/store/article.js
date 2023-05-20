import axios from 'axios';
import communityUrl from '@/api_url/communityUrl';
import router from '@/router';

const movie = {
  state: {
    allArticles: [],
    articleDetail: {},
  },
  getters: {
    getAllArticles(state) {
      return state.allArticles;
    },
    getArticleDetail(state) {
      return state.articleDetail;
    },
  },
  mutations: {
    SET_ALL_ARTICLES(state, allArticles) {
      state.allArticles = allArticles;
    },
    SET_ARTICLE_DETAIL(state, articleDetail) {
      state.articleDetail = articleDetail;
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
    fetchArticleDetail(context, articleId) {
      axios({
        method: 'get',
        url: communityUrl.articleDetail(articleId),
        headers: {
          Authorization: `Token ${context.rootState.auth.token}`,
        },
      })
        .then((res) => {
          context.commit('SET_ARTICLE_DETAIL', res.data);
        })
        .catch((err) => {
          alert(err);
        });
    },
    createComment(context, { commentInfo, articleId }) {
      axios({
        method: 'post',
        url: communityUrl.createComment(articleId),
        data: commentInfo,
        headers: {
          Authorization: `Token ${context.rootState.auth.token}`,
        },
      })
        .then((res) => {
          console.log(res);
          context.dispatch('fetchArticleDetail', articleId);
        })
        .catch((err) => {
          alert(err);
        });
    },
    delArticle(context, articleId) {
      axios({
        method: 'delete',
        url: communityUrl.articleDetail(articleId),
        headers: {
          Authorization: `Token ${context.rootState.auth.token}`,
        },
      })
        .then((res) => {
          console.log(res);
          context.commit('SET_ARTICLE_DETAIL', {});
          router.push({ name: 'community' });
        })
        .catch((err) => {
          alert(err);
        });
    },
    updateArticle(context, { articleInfo, articleId }) {
      axios({
        method: 'put',
        url: communityUrl.articleDetail(articleId),
        data: articleInfo,
        headers: {
          Authorization: `Token ${context.rootState.auth.token}`,
        },
      })
        .then((res) => {
          console.log(res);
          router.push({ name: 'article-detail', params: { articleId } });
        })
        .catch((err) => {
          alert(err);
        });
    },
    delComment(context, { articleId, commentId }) {
      axios({
        method: 'delete',
        url: communityUrl.commentDetail(articleId, commentId),
        headers: {
          Authorization: `Token ${context.rootState.auth.token}`,
        },
      })
        .then((res) => {
          console.log(res);
          context.dispatch('fetchArticleDetail', articleId);
        })
        .catch((err) => {
          alert(err);
        });
    },
    updateComment(context, { commentInfo, articleId, commentId }) {
      axios({
        method: 'put',
        url: communityUrl.commentDetail(articleId, commentId),
        data: commentInfo,
        headers: {
          Authorization: `Token ${context.rootState.auth.token}`,
        },
      })
        .then((res) => {
          console.log(res);
          context.dispatch('fetchArticleDetail', articleId);
        })
        .catch((err) => {
          alert(err);
        });
    },
    fetchToggleLike(context, articleId) {
      axios({
        method: 'post',
        url: communityUrl.likeArticle(articleId),
        data: { like_users: [context.rootState.auth.curUser.pk] },
        headers: {
          Authorization: `Token ${context.rootState.auth.token}`,
        },
      })
        .then((res) => {
          console.log(res);
          context.dispatch('fetchArticleDetail', articleId);
        })
        .catch((err) => {
          alert(err);
        });
    },
  },
};

export default movie;
