<template>
  <div>
    <h1 class="mt-3" style="color: var(--bs-red)">Community Articles</h1>
    <ArticleItem />
  </div>
</template>

<script>
import ArticleItem from '@/components/ArticleItem.vue.js';
export default {
  name: 'CommunityView',
  components: {
    ArticleItem,
  },
};
</script>

<style></style>
