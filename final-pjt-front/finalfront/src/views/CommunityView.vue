<template>
  <div class="ms-5">
    <div class="d-flex justify-content-around align-items-center">
      <h1 class="mt-5 mb-5" style="color: var(--bs-red)">Community Articles</h1>
      <button
        v-if="isLogin"
        class="button h-75"
        @click="routeCreateArticlePage"
      >
        글 작성하기
      </button>
    </div>

    <div class="article-grid">
      <ArticleItem
        v-for="(item, index) in paginatedArticles"
        :key="index"
        :article-info="item"
      />
    </div>

    <nav v-if="totalPages > 1" class="pagination-container">
      <ul class="pagination">
        <li
          class="page-item"
          :class="{ active: page === currentPage }"
          v-for="page in totalPages"
          :key="page"
        >
          <a class="page-link" @click="changePage(page)">{{ page }}</a>
        </li>
      </ul>
    </nav>
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
    paginatedArticles() {
      const startIndex = (this.currentPage - 1) * this.itemsPerPage;
      const endIndex = startIndex + this.itemsPerPage;
      return this.getAllArticles.slice(startIndex, endIndex);
    },
    totalPages() {
      return Math.ceil(this.getAllArticles.length / this.itemsPerPage);
    },
  },
  data() {
    return {
      currentPage: 1,
      itemsPerPage: 6,
    };
  },
  methods: {
    ...mapActions(['fetchAllArticles']),
    routeCreateArticlePage() {
      this.$router.push({ name: 'article-create' });
    },
    changePage(page) {
      this.currentPage = page;
    },
  },
  created() {
    this.fetchAllArticles();
  },
};
</script>

<style>
.article-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  grid-gap: 20px;
  min-height: 436.56px;
}

.pagination-container {
  display: flex;
  justify-content: center;
  align-items: center;
  /* 페이지네이션 컨테이너의 최소 높이 설정 */
}

.pagination {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-right: 80px;
}
</style>
