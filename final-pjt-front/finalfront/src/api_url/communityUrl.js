const COMMUNITY_HOST = 'http://127.0.0.1:8000/community/';

export default {
  createArticle: () => COMMUNITY_HOST,
  getAllArticles: () => COMMUNITY_HOST + 'all/',
  getArticleDetail: (articleId) => COMMUNITY_HOST + `${articleId}/`,
  createComment: (articleId) => COMMUNITY_HOST + `${articleId}/` + 'comment/',
};
