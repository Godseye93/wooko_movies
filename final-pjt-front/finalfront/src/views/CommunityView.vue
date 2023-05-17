<template>
  <div class="text-center">
    <h1 class="mt-3 mb-5" style="color: var(--bs-red)">Community Articles</h1>
    <button class="button border-0" @click="routeCreateArticlePage">
      글 작성하기
    </button>
    <ArticleItem />
  </div>
</template>

<script>
import ArticleItem from '@/components/ArticleItem.vue';

export default {
  name: 'CommunityView',
  components: {
    ArticleItem,
  },
  methods: {
    routeCreateArticlePage() {
      this.$router.push({ name: 'article-create' });
    },
  },
};
</script>

<style></style>
