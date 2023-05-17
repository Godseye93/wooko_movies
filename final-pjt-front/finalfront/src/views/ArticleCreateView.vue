<template>
  <div class="mt-3">
    <div class="contact_2l row">
      <div class="col-md-12">
        <h4>글 작성하기</h4>
      </div>
    </div>

    <div class="contact_2l1 mt-3 row">
      <div class="col-md-6">
        <div class="contact_2l1i">
          <input class="form-control" placeholder="제목*" type="text" />
        </div>
      </div>
    </div>

    <div class="contact_2l1 mt-3 row">
      <div class="col-md-12">
        <div class="contact_2l1i">
          <textarea
            placeholder="내용을 입력하세요."
            class="form-control form_text"
          ></textarea>
          <h6 class="mt-3 mb-3">
            <a class="button" href="#" @click="submitArticle"> Submit</a>
          </h6>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ArticleCreateView',
  methods: {
    submitArticle() {},
  },
};
</script>

<style></style>
