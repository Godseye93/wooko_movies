<template>
  <div class="blog_1l4 mt-3">
    <SearchMovieItem
      v-for="(item, index) in getSearchedMovies"
      :key="index"
      :movie-info="item"
      class="mb-4"
    />
  </div>
</template>

<script>
import SearchMovieItem from '@/components/SearchMovieItem.vue';
import { mapGetters, mapActions } from 'vuex';

export default {
  components: {
    SearchMovieItem,
  },

  computed: {
    ...mapGetters(['getSearchedMovies']),
  },
  methods: {
    ...mapActions(['fetchSearchMovies']),
  },
  created() {
    this.fetchSearchMovies(this.$route.params.keyword);
  },
};
</script>

<style></style>
