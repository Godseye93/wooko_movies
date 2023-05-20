<template>
  <div class="blog_1l1i mt-3" @click="articleDetail">
    <h2 class="mt-3 ms-3">{{ articleInfo.title }}</h2>
    <h6 class="fw-normal mt-3 col_light">
      <span class="ms-3"> 작성 날짜 : {{ createdFormatDate }}</span>
      <span class="ms-3"> 수정 날짜 : {{ updatedFormatDate }}</span>
      <span class="ms-3"> 댓글 {{ articleInfo.comments.length }}개</span>
      <span class="ms-3"> 좋아요 {{ articleInfo.like_users.length }} 개</span>
    </h6>
  </div>
</template>

<script>
import formatDate from '@/util/formatDate';

export default {
  name: 'ArticleItem',
  props: {
    articleInfo: {
      type: Object,
      required: true,
    },
  },
  computed: {
    createdFormatDate() {
      return formatDate(this.articleInfo.created_at);
    },
    updatedFormatDate() {
      return formatDate(this.articleInfo.updated_at);
    },
  },
  methods: {
    articleDetail() {
      this.$router.push({
        name: 'article-detail',
        params: { articleId: this.articleInfo.id },
      });
    },
  },
};
</script>

<style></style>
