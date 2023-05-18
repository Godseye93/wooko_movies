<template>
  <div class="row blog_1">
    <div class="col-md-8 my-auto">
      <div class="blog_1l">
        <div class="blog_1l1">
          <div class="popular_2i1lm position-relative clearfix">
            <div class="popular_2i1lm1 clearfix">
              <div class="grid">
                <figure class="effect-jazz mb-0">
                  <a href="#"
                    ><img
                      :src="imgBaseUrlMain + getMovieDetail.backdrop_path"
                      height="450"
                      class="w-100"
                      alt="img25"
                  /></a>
                </figure>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="col-md-4">
      <div class="blog_1r">
        <div class="blog_1r1 p-4 mt-4">
          <h4>{{ getMovieDetail.title }}</h4>
          <hr class="line mb-4 border-0" />
          <div class="popular_2i1r">
            <br />

            <h6>
              <span class="ms-2"
                ><svg
                  xmlns="http://www.w3.org/2000/svg"
                  width="16"
                  height="16"
                  fill="currentColor"
                  class="bi bi-calendar"
                  viewBox="0 0 16 16"
                >
                  <path
                    d="M3.5 0a.5.5 0 0 1 .5.5V1h8V.5a.5.5 0 0 1 1 0V1h1a2 2 0 0 1 2 2v11a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V3a2 2 0 0 1 2-2h1V.5a.5.5 0 0 1 .5-.5zM1 4v10a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1V4H1z"
                  />
                </svg>
              </span>
              출시일 : {{ getMovieDetail.release_date }}
            </h6>
            <br />
            <p>
              {{ getMovieDetail.overview }}
            </p>

            <div class="blog_1r1 p-4 mt-4 ps-0">
              <h4>Popular <span class="col_red">Tags</span></h4>
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
          <div class="col-md-6 ms-0">
            <div class="play2rir">
              <h6 class="fw-normal">
                인기도 - {{ getMovieDetail.popularity }}
              </h6>
              <div class="progress">
                <div
                  class="progress-bar"
                  role="progressbar"
                  :style="{ width: `${getMovieDetail.popularity / 30}%` }"
                  aria-valuenow="25"
                  aria-valuemin="0"
                  aria-valuemax="100"
                ></div>
              </div>
              <h6 class="fw-normal mt-3">
                평점 - {{ getMovieDetail.vote_average }}
              </h6>
              <div class="progress mb-5">
                <div
                  class="progress-bar"
                  role="progressbar"
                  :style="{ width: `${getMovieDetail.vote_average * 10}%` }"
                  aria-valuenow="25"
                  aria-valuemin="0"
                  aria-valuemax="100"
                ></div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';
export default {
  name: 'MovieDetailView',
  data() {
    return {
      imgBaseUrlMain: 'https://image.tmdb.org/t/p/w500/',
    };
  },

  computed: {
    ...mapGetters(['getMovieDetail']),
  },
  methods: {
    ...mapActions(['fetchMovieDetail']),
  },
  created() {
    if (this.$route.params.movieId) {
      this.fetchMovieDetail(this.$route.params.movieId);
    }
  },
};
</script>

<style>
.blog_1r1 ul li a {
  font-size: 14px;
  padding: 7px 12px 6px;
  background: #252525;
  margin: 0px 2px 6px 0px;
  cursor: pointer;
}
</style>
