<template>
  <div class="blog_1l1i mt-3 mx-3">
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
    <p class="mt-3">
      Consectetuer adipiscing elit sedare diam nonummy nibh euismod estat
      tinciduntal ut laoreet dolore magna aliquam erat volutpat. Ut wisi enim ad
      minimatisa veniam, quis nostrud exerci tation ullamcorper suscipit
      lobortis nisl. Name liber tempor cum soluta nobis eleifend option congue
      nihil imperdietes
    </p>
    <div v-if="isLiked">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        width="32"
        height="32"
        fill="currentColor"
        class="bi bi-heart-fill mb-5 mt-3"
        viewBox="0 0 16 16"
        @click="toggleLike"
        style="fill: red"
      >
        <path
          fill-rule="evenodd"
          d="M8 1.314C12.438-3.248 23.534 4.735 8 15-7.534 4.736 3.562-3.248 8 1.314z"
        />
      </svg>
    </div>
    <div v-else>
      <svg
        xmlns="http://www.w3.org/2000/svg"
        width="32"
        height="32"
        fill="currentColor"
        class="bi bi-heart mb-3 mt-3"
        viewBox="0 0 16 16"
        @click="toggleLike"
        style="fill: red"
      >
        <path
          d="m8 2.748-.717-.737C5.6.281 2.514.878 1.4 3.053c-.523 1.023-.641 2.5.314 4.385.92 1.815 2.834 3.989 6.286 6.357 3.452-2.368 5.365-4.542 6.286-6.357.955-1.886.838-3.362.314-4.385C13.486.878 10.4.28 8.717 2.01L8 2.748zM8 15C-7.333 4.868 3.279-3.04 7.824 1.143c.06.055.119.112.176.171a3.12 3.12 0 0 1 .176-.17C12.72-3.042 23.333 4.867 8 15z"
        />
      </svg>
    </div>
    <div>
      <input
        type="username"
        id="username"
        class="form-control bg-transparent d-inline-block w-75 me-3"
        placeholder="Username"
      />

      <h6 class="font_14 mb-3 mt-3 d-inline-block">
        <a class="button p-3 pt-2 pb-2" href="#"> Reply</a>
      </h6>
    </div>
    <CommentItem />
    <CommentItem />
    <CommentItem />
  </div>
</template>

<script>
import CommentItem from '@/components/CommentItem.vue';
export default {
  name: 'ArticleDetailView',
  components: {
    CommentItem,
  },
  data() {
    return {
      isLiked: false,
    };
  },
  methods: {
    toggleLike() {
      this.isLiked = !this.isLiked;
    },
  },
};
</script>

<style></style>
