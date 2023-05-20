const COMMUNITY_HOST = 'http://127.0.0.1:8000/community/';

export default {
  createArticle: () => COMMUNITY_HOST,
  getAllArticles: () => COMMUNITY_HOST + 'all/',
  articleDetail: (articleId) => COMMUNITY_HOST + `${articleId}/`,
  createComment: (articleId) => COMMUNITY_HOST + `${articleId}/` + 'comment/',
  commentDetail: (articleId, commentId) =>
    COMMUNITY_HOST + `${articleId}/` + 'comment/' + `${commentId}/`,
  likeArticle: (articleId) => COMMUNITY_HOST + `${articleId}/` + 'like/',
};
