<template>
  <div class="blog_1l1i mt-5" @click="articleDetail">
    <h2 class="mt-3">Company Foundation Provides Grant to Emory Law</h2>
    <h6 class="fw-normal mt-3 col_light">
      <span
        ><i class="fa fa-clock-o me-1 align-middle col_red"></i> 14 December
        2021</span
      >
      <span class="ms-3"
        ><i class="fa fa-user me-1 align-middle col_red"></i> Admin</span
      >
      <span class="ms-3"
        ><i class="fa fa-comment me-1 align-middle col_red"></i> Comment</span
      >
    </h6>
  </div>
</template>

<script>
export default {
  name: 'ArticleItem',
  methods: {
    articleDetail() {
      this.$router.push({ name: 'article-detail' });
    },
  },
};
</script>

<style></style>
