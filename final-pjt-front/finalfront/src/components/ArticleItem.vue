<template>
  <div class="blog_1l1i mt-5" @click="articleDetail">
    <h2 class="mt-3">{{ articleInfo.title }}</h2>
    <h6 class="fw-normal mt-3 col_light">
      <span>{{ articleInfo.created_at }}</span>
      <span class="ms-3"> {{ articleInfo.content }}</span>
      <span class="ms-3"> Comment</span>
    </h6>
  </div>
</template>

<script>
export default {
  name: 'ArticleItem',
  props: {
    articleInfo: {
      type: Object,
      required: true,
    },
  },
  methods: {
    articleDetail() {
      this.$router.push({ name: 'article-detail' });
    },
  },
};
</script>

<style></style>
