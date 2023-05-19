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
    <ArticleItem
      v-for="(item, index) in getAllArticles"
      :key="index"
      :article-info="item"
    />
  </div>
</template>

<script>
import ArticleItem from '@/components/ArticleItem.vue';
import { mapGetters, mapActions } from 'vuex';

export default {
  name: 'CommunityView',
  components: {
    ArticleItem,
  },
  computed: {
    ...mapGetters(['isLogin', 'getAllArticles']),
  },
  methods: {
    ...mapActions(['fetchAllArticles']),
    routeCreateArticlePage() {
      this.$router.push({ name: 'article-create' });
    },
  },
  created() {
    this.fetchAllArticles();
  },
};
</script>

<style></style>
