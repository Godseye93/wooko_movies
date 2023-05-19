<template>
  <div class="text-center">
    <h1 class="mt-3 mb-5" style="color: var(--bs-red)">Community Articles</h1>
    <button
      v-if="isLogin"
      class="button border-0"
      @click="routeCreateArticlePage"
    >
      글 작성하기
    </button>
    <ArticleItem />
  </div>
</template>

<script>
import ArticleItem from '@/components/ArticleItem.vue';
import { mapGetters } from 'vuex';

export default {
  name: 'CommunityView',
  components: {
    ArticleItem,
  },
  computed: {
    ...mapGetters(['isLogin']),
  },
  methods: {
    routeCreateArticlePage() {
      this.$router.push({ name: 'article-create' });
    },
  },
};
</script>

<style></style>
