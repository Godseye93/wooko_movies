<template>
  <div class="blog_1l1i mt-3 mx-3 ms-5">
    <h2 class="mt-3">{{ getArticleDetail.title }}</h2>

    <p class="mt-3">
      {{ getArticleDetail.content }}
    </p>
    <h6 class="fw-normal mt-3 col_light d-inline-block me-3">
      <span class="me-4">글 작성 날짜 : {{ createdFormatDate }}</span>
      <span>글 수정 날짜 : {{ updatedFormatDate }}</span>
      <span class="ms-3">
        Comment : {{ getArticleDetail.comments.length }}개</span
      >
    </h6>
    <span v-if="isLiked">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        width="32"
        height="32"
        fill="currentColor"
        class="bi bi-heart-fill mb-3 mt-3"
        viewBox="0 0 16 16"
        @click="toggleLike"
        style="fill: red"
      >
        <path
          fill-rule="evenodd"
          d="M8 1.314C12.438-3.248 23.534 4.735 8 15-7.534 4.736 3.562-3.248 8 1.314z"
        />
      </svg>
    </span>
    <span v-else>
      <svg
        xmlns="http://www.w3.org/2000/svg"
        width="32"
        height="32"
        fill="currentColor"
        class="bi bi-heart mb-3 mt-3"
        viewBox="0 0 16 16"
        @click="toggleLike"
        style="fill: red"
      >
        <path
          d="m8 2.748-.717-.737C5.6.281 2.514.878 1.4 3.053c-.523 1.023-.641 2.5.314 4.385.92 1.815 2.834 3.989 6.286 6.357 3.452-2.368 5.365-4.542 6.286-6.357.955-1.886.838-3.362.314-4.385C13.486.878 10.4.28 8.717 2.01L8 2.748zM8 15C-7.333 4.868 3.279-3.04 7.824 1.143c.06.055.119.112.176.171a3.12 3.12 0 0 1 .176-.17C12.72-3.042 23.333 4.867 8 15z"
        />
      </svg>
    </span>
    <div v-if="isAuthor">
      <button class="button p-3 pt-2 pb-2 me-3" @click="routeUpdateArticle">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="16"
          height="16"
          fill="currentColor"
          class="bi bi-pencil-square me-2"
          viewBox="0 0 16 16"
        >
          <path
            d="M15.502 1.94a.5.5 0 0 1 0 .706L14.459 3.69l-2-2L13.502.646a.5.5 0 0 1 .707 0l1.293 1.293zm-1.75 2.456-2-2L4.939 9.21a.5.5 0 0 0-.121.196l-.805 2.414a.25.25 0 0 0 .316.316l2.414-.805a.5.5 0 0 0 .196-.12l6.813-6.814z"
          />
          <path
            fill-rule="evenodd"
            d="M1 13.5A1.5 1.5 0 0 0 2.5 15h11a1.5 1.5 0 0 0 1.5-1.5v-6a.5.5 0 0 0-1 0v6a.5.5 0 0 1-.5.5h-11a.5.5 0 0 1-.5-.5v-11a.5.5 0 0 1 .5-.5H9a.5.5 0 0 0 0-1H2.5A1.5 1.5 0 0 0 1 2.5v11z"
          />
        </svg>
        <span>글 수정하기</span>
      </button>
      <button
        class="button p-3 pt-2 pb-2"
        @click="delArticle(getArticleDetail.id)"
      >
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="16"
          height="16"
          fill="currentColor"
          class="bi bi-trash me-2"
          viewBox="0 0 16 16"
        >
          <path
            d="M5.5 5.5A.5.5 0 0 1 6 6v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5Zm2.5 0a.5.5 0 0 1 .5.5v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5Zm3 .5a.5.5 0 0 0-1 0v6a.5.5 0 0 0 1 0V6Z"
          />
          <path
            d="M14.5 3a1 1 0 0 1-1 1H13v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V4h-.5a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1H6a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1h3.5a1 1 0 0 1 1 1v1ZM4.118 4 4 4.059V13a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1V4.059L11.882 4H4.118ZM2.5 3h11V2h-11v1Z"
          />
        </svg>
        <span>글 삭제하기</span>
      </button>
    </div>
    <div>
      <input
        type="username"
        id="username"
        class="form-control bg-transparent d-inline-block w-75 me-3"
        placeholder="댓글을 입력하세요"
        v-model="commentInfo.content"
        @keyup.enter="createComment(commentInfo, getArticleDetail.id)"
      />

      <h6 class="font_14 mb-3 mt-3 d-inline-block">
        <button
          class="button p-3 pt-2 pb-2"
          @click="createComment(commentInfo, getArticleDetail.id)"
        >
          Reply
        </button>
      </h6>
    </div>
    <CommentItem />
    <CommentItem />
    <CommentItem />
  </div>
</template>

<script>
import CommentItem from '@/components/CommentItem.vue';
import { mapActions, mapGetters } from 'vuex';
import formatDate from '@/util/formatDate';

export default {
  name: 'ArticleDetailView',
  components: {
    CommentItem,
  },
  data() {
    return {
      isLiked: false,
      commentInfo: {
        content: null,
      },
    };
  },
  computed: {
    ...mapGetters(['getArticleDetail', 'getCurUser']),
    createdFormatDate() {
      return formatDate(this.getArticleDetail.created_at);
    },
    updatedFormatDate() {
      return formatDate(this.getArticleDetail.updated_at);
    },
    isAuthor() {
      return this.getCurUser.pk === this.getArticleDetail.user;
    },
  },

  methods: {
    ...mapActions(['fetchArticleDetail', 'createComment', 'delArticle']),
    toggleLike() {
      this.isLiked = !this.isLiked;
    },
    routeUpdateArticle() {
      this.$router.push({
        name: 'article-update',
        params: { articleId: this.getArticleDetail.id },
      });
    },
  },
  created() {
    this.fetchArticleDetail(this.$route.params.articleId);
  },
};
</script>

<style></style>
