<template>
  <div class="popular_2i1 row">
    <div class="col-md-4 col-4">
      <div class="popular_2i1lm position-relative clearfix">
        <div class="popular_2i1lm1 clearfix">
          <div class="grid">
            <figure class="effect-jazz mb-0">
              <router-link
                :to="{ name: 'movie-detail', params: { id: movieInfo.id } }"
                ><img
                  :src="imgBaseUrlMain + movieInfo.poster_path"
                  class="w-100"
                  alt="img25"
              /></router-link>
            </figure>
          </div>
        </div>
        <div
          class="popular_2i1lm2 position-absolute top-0 w-100 text-center clearfix"
        ></div>
      </div>
    </div>
    <div class="col-md-8 col-8 my-auto">
      <div class="popular_2i1r">
        <h5 class="col_red">{{ movieInfo.title }}</h5>
        <h6>Action, Thriller</h6>
        <h6>
          Imdb 8.3
          <span class="ms-2"><i class="fa fa-star col_red me-1"></i></span> Year
          : 2022 <span class="ms-2">Runtime: 2h 29m</span>
        </h6>
        <p>
          {{ movieInfo.overview }}
        </p>
      </div>
      <div class="blog_1r1 p-4 mt-4 ps-0">
        <h4>genres <span class="col_red">Tags</span></h4>
        <hr class="line mb-4 border-0" />
        <ul class="mb-0">
          <li class="d-inline-block">
            <a class="d-block">Analyze</a>
          </li>
          <li class="d-inline-block">
            <a class="d-block">Audio</a>
          </li>
          <li class="d-inline-block">
            <a class="d-block">Blog</a>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SearchMovieItem',
  data() {
    return {
      imgBaseUrlMain: 'https://image.tmdb.org/t/p/w500/',
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

<style></style>
