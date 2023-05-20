<template>
  <div class="mt-3 ms-5 me-5">
    <div class="contact_2l row">
      <div class="col-md-12">
        <h4>글 수정하기</h4>
      </div>
    </div>

    <div class="contact_2l1 mt-3 row">
      <div class="col-md-6">
        <div class="contact_2l1i">
          <input
            class="form-control"
            placeholder="제목*"
            type="text"
            v-model="articleInfo.title"
          />
        </div>
      </div>
    </div>

    <div class="contact_2l1 mt-3 row">
      <div class="col-md-12">
        <div class="contact_2l1i">
          <textarea
            placeholder="내용을 입력하세요."
            class="form-control form_text"
            v-model="articleInfo.content"
          ></textarea>
          <h6 class="mt-3 mb-3">
            <button
              class="button"
              @click="
                updateArticle({ articleInfo, articleId: getArticleDetail.id })
              "
            >
              수정하기
            </button>
          </h6>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex';
export default {
  name: 'ArticleUpdateView',
  data() {
    return {
      articleInfo: {
        title: null,
        content: null,
      },
    };
  },

  computed: {
    ...mapGetters(['getArticleDetail']),
  },
  methods: {
    ...mapActions(['updateArticle', 'fetchArticleDetail']),
  },
  created() {
    if (this.$route.params.articleId) {
      this.fetchArticleDetail(this.$route.params.articleId);
      this.articleInfo.title = this.getArticleDetail.title;
      this.articleInfo.content = this.getArticleDetail.content;
    }
  },
};
</script>

<style></style>
