<template>
  <div class="col-md-3 col-6">
    <div class="trend_2im clearfix position-relative">
      <div class="trend_2im1 clearfix">
        <figure class="effect-jazz mb-0">
          <router-link
            :to="{ name: 'movie-detail', params: { movieId: movieInfo.id } }"
            ><img
              style="object-fit: cover; height: 260px"
              :src="imgBaseUrlMain + movieInfo.poster_path"
              class="w-100"
              alt="img"
          /></router-link>
        </figure>
      </div>
      <div
        class="trend_2im2 clearfix text-center position-absolute w-100 top-0"
      >
        <span class="fs-1"
          ><a class="col_red" href="#"><i class="fa fa-youtube-play"></i></a
        ></span>
      </div>
    </div>
    <div class="trend_2ilast bg_grey p-3 clearfix">
      <h5>
        <router-link
          :to="{ name: 'movie-detail', params: { movieId: movieInfo.id } }"
          ><p class="overview-title col_red">
            {{ movieInfo.title }}
          </p></router-link
        >
      </h5>
      <p class="mb-2 overview-text">
        {{ movieInfo.overview }}
      </p>
      <span class="col_red">
        평점 :
        <span
          v-for="index in Math.floor(movieInfo.vote_average / 2)"
          :key="index"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="16"
            height="16"
            fill="currentColor"
            class="bi bi-star-fill"
            viewBox="0 0 16 16"
          >
            <path
              d="M3.612 15.443c-.386.198-.824-.149-.746-.592l.83-4.73L.173 6.765c-.329-.314-.158-.888.283-.95l4.898-.696L7.538.792c.197-.39.73-.39.927 0l2.184 4.327 4.898.696c.441.062.612.636.282.95l-3.522 3.356.83 4.73c.078.443-.36.79-.746.592L8 13.187l-4.389 2.256z"
            />
          </svg>
        </span>
        <span
          v-if="
            movieInfo.vote_average / 2 -
              Math.floor(movieInfo.vote_average / 2) >=
            0.5
          "
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="16"
            height="16"
            fill="currentColor"
            class="bi bi-star-half"
            viewBox="0 0 16 16"
          >
            <path
              d="M5.354 5.119 7.538.792A.516.516 0 0 1 8 .5c.183 0 .366.097.465.292l2.184 4.327 4.898.696A.537.537 0 0 1 16 6.32a.548.548 0 0 1-.17.445l-3.523 3.356.83 4.73c.078.443-.36.79-.746.592L8 13.187l-4.389 2.256a.52.52 0 0 1-.146.05c-.342.06-.668-.254-.6-.642l.83-4.73L.173 6.765a.55.55 0 0 1-.172-.403.58.58 0 0 1 .085-.302.513.513 0 0 1 .37-.245l4.898-.696zM8 12.027a.5.5 0 0 1 .232.056l3.686 1.894-.694-3.957a.565.565 0 0 1 .162-.505l2.907-2.77-4.052-.576a.525.525 0 0 1-.393-.288L8.001 2.223 8 2.226v9.8z"
            />
          </svg>
        </span>
      </span>

      <h6 class="fw-normal mt-3 col_light">
        <span
          ><i class="fa fa-clock-o me-1 align-middle col_red"></i>
          {{ movieInfo.release_date }}</span
        >

        <span class="ms-3"
          ><i class="fa fa-comment me-1 align-middle col_red"></i> 인기 :
          {{ movieInfo.popularity }}</span
        >
      </h6>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MovieItem',
  data() {
    return {
      imgBaseUrlMain: 'https://image.tmdb.org/t/p/w500/',
      startCnt: [],
    };
  },

  props: {
    movieInfo: {
      type: Object,
      required: true,
    },
  },
};
</script>

<style>
.overview-text {
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 2; /* Number of lines to display */
  overflow: hidden;
  text-overflow: ellipsis;
}

.overview-title {
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 1; /* Number of lines to display */
  overflow: hidden;
  text-overflow: ellipsis;
}
</style>
