<template>
  <div class="home">
    <section id="center" class="center_home">
      <h4 class="mb-0 mt-5 ms-3">
        내 맞춤 추천 <span class="col_red">Movies</span>
        <p class="mt-3">
          <span
            ><svg
              xmlns="http://www.w3.org/2000/svg"
              width="16"
              height="16"
              fill="currentColor"
              class="bi bi-exclamation-circle me-2 text-danger"
              viewBox="0 0 16 16"
            >
              <path
                d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z"
              />
              <path
                d="M7.002 11a1 1 0 1 1 2 0 1 1 0 0 1-2 0zM7.1 4.995a.905.905 0 1 1 1.8 0l-.35 3.507a.552.552 0 0 1-1.1 0L7.1 4.995z"
              />
            </svg>
          </span>
          <span class="fs-6"
            >MINI GAME이 반영된 추천 목록입니다, MINI GAME 이력이 없을 경우
            임의의 영화가 추천 됩니다</span
          >
        </p>
        <button
          class="button rounded fs-6 me-3"
          @click="fetchRecommendedMovies('genre_recommend')"
        >
          장르별 추천</button
        ><button
          class="button rounded fs-6 me-3"
          @click="fetchRecommendedMovies('actor_recommend')"
        >
          배우별 추천</button
        ><button
          class="button rounded fs-6"
          @click="fetchRecommendedMovies('director_recommend')"
        >
          감독별 추천
        </button>
      </h4>
      <div
        id="carouselExampleCaptions"
        class="carousel slide"
        data-bs-ride="carousel"
      >
        <div class="carousel-indicators">
          <button
            type="button"
            data-bs-target="#carouselExampleCaptions"
            data-bs-slide-to="0"
            class="active"
            aria-label="Slide 1"
          ></button>
          <button
            type="button"
            data-bs-target="#carouselExampleCaptions"
            data-bs-slide-to="1"
            aria-label="Slide 2"
            class=""
            aria-current="true"
          ></button>
          <button
            type="button"
            data-bs-target="#carouselExampleCaptions"
            data-bs-slide-to="2"
            aria-label="Slide 3"
          ></button>
        </div>
        <div class="carousel-inner mt-3">
          <div class="carousel-item active">
            <img
              v-if="getRecommendedMovies[0]"
              :src="baseImgUrl + getRecommendedMovies[0].backdrop_path"
              class="d-block w-100 center-img"
              alt="..."
            />
            <div
              class="carousel-caption d-md-block"
              style="text-align: left; padding: 220px; bottom: 0; left: 0"
            >
              <h1 class="font_60">{{ getRecommendedMovies[0]?.title }}</h1>
              <h6 class="mt-3">
                츨시일 : {{ getRecommendedMovies[0]?.release_date }}
                <h6 class="mt-4">
                  <router-link
                    class="button"
                    :to="{
                      name: 'movie-detail',
                      params: { movieId: getRecommendedMovies[0]?.id },
                    }"
                  >
                    자세히 보기</router-link
                  >
                </h6>
              </h6>
              <p class="mt-3 overview-text-home">
                {{ getRecommendedMovies[0]?.overview }}
              </p>
              <p class="mb-2">
                <span class="col_red me-1 fw-bold">인기도:</span>
                {{ getRecommendedMovies[0]?.popularity }}
              </p>
              <p class="mb-2">
                <span class="col_red me-1 fw-bold">평점:</span>
                {{ getRecommendedMovies[0]?.vote_average }}
              </p>
              <p class="mb-2">
                <span class="col_red me-1 fw-bold">Genres:</span>
                <span
                  v-for="(item, index) in getRecommendedMovies[0]?.genre_ids"
                  :key="index"
                  >{{ item.name }},
                </span>
              </p>
            </div>
          </div>

          <div class="carousel-item">
            <img
              v-if="getRecommendedMovies[1]"
              :src="baseImgUrl + getRecommendedMovies[1].backdrop_path"
              class="d-block w-100 center-img"
              alt="..."
            />
            <div
              class="carousel-caption d-md-block"
              style="text-align: left; padding: 220px; bottom: 0; left: 0"
            >
              <h1 class="font_60">{{ getRecommendedMovies[1]?.title }}</h1>
              <h6 class="mt-3">
                츨시일 : {{ getRecommendedMovies[1]?.release_date }}
                <h6 class="mt-4">
                  <router-link
                    class="button"
                    :to="{
                      name: 'movie-detail',
                      params: { movieId: getRecommendedMovies[1]?.id },
                    }"
                  >
                    자세히 보기</router-link
                  >
                </h6>
              </h6>
              <p class="mt-3 overview-text-home">
                {{ getRecommendedMovies[1]?.overview }}
              </p>
              <p class="mb-2">
                <span class="col_red me-1 fw-bold">인기도:</span>
                {{ getRecommendedMovies[1]?.popularity }}
              </p>
              <p class="mb-2">
                <span class="col_red me-1 fw-bold">평점:</span>
                {{ getRecommendedMovies[1]?.vote_average }}
              </p>
              <p class="mb-2">
                <span class="col_red me-1 fw-bold">Genres:</span>
                <span
                  v-for="(item, index) in getRecommendedMovies[1]?.genre_ids"
                  :key="index"
                  >{{ item.name }},
                </span>
              </p>
            </div>
          </div>

          <div class="carousel-item">
            <img
              v-if="getRecommendedMovies[2]"
              :src="baseImgUrl + getRecommendedMovies[2].backdrop_path"
              class="d-block w-100 center-img"
              alt="..."
            />
            <div
              class="carousel-caption d-md-block"
              style="text-align: left; padding: 220px; bottom: 0; left: 0"
            >
              <h1 class="font_60">{{ getRecommendedMovies[2]?.title }}</h1>
              <h6 class="mt-3">
                츨시일 : {{ getRecommendedMovies[2]?.release_date }}
                <h6 class="mt-4">
                  <router-link
                    class="button"
                    :to="{
                      name: 'movie-detail',
                      params: { movieId: getRecommendedMovies[2]?.id },
                    }"
                  >
                    자세히 보기</router-link
                  >
                </h6>
              </h6>
              <p class="mt-3 overview-text-home">
                {{ getRecommendedMovies[2]?.overview }}
              </p>
              <p class="mb-2">
                <span class="col_red me-1 fw-bold">인기도:</span>
                {{ getRecommendedMovies[2]?.popularity }}
              </p>
              <p class="mb-2">
                <span class="col_red me-1 fw-bold">평점:</span>
                {{ getRecommendedMovies[2]?.vote_average }}
              </p>
              <p class="mb-2">
                <span class="col_red me-1 fw-bold">Genres:</span>
                <span
                  v-for="(item, index) in getRecommendedMovies[2]?.genre_ids"
                  :key="index"
                  >{{ item.name }},
                </span>
              </p>
            </div>
          </div>
        </div>
        <button
          class="carousel-control-prev"
          type="button"
          data-bs-target="#carouselExampleCaptions"
          data-bs-slide="prev"
        >
          <span class="carousel-control-prev-icon" aria-hidden="true"></span>
          <span class="visually-hidden">Previous</span>
        </button>
        <button
          class="carousel-control-next"
          type="button"
          data-bs-target="#carouselExampleCaptions"
          data-bs-slide="next"
        >
          <span class="carousel-control-next-icon" aria-hidden="true"></span>
          <span class="visually-hidden">Next</span>
        </button>
      </div>
    </section>
    <MovieListVue
      category="평점 순"
      :movieInfoList="getHighRatingMovies"
      slideId="carouselExampleCaptions2"
    />
    <MovieListVue
      category="최신 순"
      :movieInfoList="getLatestMovies"
      slideId="carouselExampleCaptions3"
      class="mb-5"
    />
  </div>
</template>
<script>
import MovieListVue from '../components/MovieList.vue';
import { mapGetters, mapActions } from 'vuex';
// @ is an alias to /src

export default {
  name: 'HomeView',
  components: { MovieListVue },
  data() {
    return {
      baseImgUrl: 'https://image.tmdb.org/t/p/w500/',
    };
  },

  computed: {
    ...mapGetters([
      'getHighRatingMovies',
      'getLatestMovies',
      'getRecommendedMovies',
      'isLogin',
    ]),
  },
  methods: {
    ...mapActions(['getSortedMovies', 'fetchRecommendedMovies']),
  },
  created() {
    if (this.isLogin) this.fetchRecommendedMovies('genre_recommend');
    else this.getSortedMovies('popularity');
    this.getSortedMovies('vote_average');
    this.getSortedMovies('release_date');
  },
};
</script>

<style>
/*
HomeView.vue
Template Name: Planet
File: Layout CSS
Author: TemplatesOnWeb
Author URI: https://www.templateonweb.com/
Licence: <a href="https://www.templateonweb.com/license">Website Template Licence</a>
*/
/*********************center_home****************/
.center-img {
  margin: 0;
}
.overview-text-home {
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 8; /* Number of lines to display */
  overflow: hidden;
  text-overflow: ellipsis;
}

.center-img {
  max-width: 1600px;
  max-height: 800px;
}
.carousel-item {
  position: relative;
}
.carousel-caption {
  text-align: left;
  background-color: rgba(0, 0, 0, 0.7);
  padding: 150px 150px;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 100%;
  color: #fff;
}
.carousel-caption p {
  width: 45%;
}
.carousel-indicators {
  bottom: 0;
}

/*********************center_home_end****************/

/*********************trend****************/

#trend .carousel-indicators {
  bottom: -50px;
}
.trend_2im2 {
  padding-top: 70px;
}

#upcome .carousel-indicators {
  bottom: -50px;
}
#upcome .trend_2im2 {
  padding-top: 90px;
}

/*********************trend_end****************/

/*********************popular****************/
.popular_1 .nav-tabs .nav-link {
  color: #fff;
  border: none;
  display: block;
  margin-left: 8px;
  margin-right: 8px;
  padding: 0;
  text-transform: uppercase;
  border-radius: 0;
  background: none;
  border-bottom: 2px solid transparent;
  padding-bottom: 8px;
}
.popular_1 .nav-tabs .nav-link:hover {
  color: #fff;
  border-bottom: 2px solid #de1002;
}
.popular_1 .nav-tabs .nav-link.active {
  color: #fff;
  border-bottom: 2px solid #de1002;
}

#choice .trend_2im2 {
  padding: 130px 15px 0px 15px !important;
  background-color: rgba(0, 0, 0, 0.7);
  height: 100%;
}
#choice .carousel-indicators {
  bottom: -50px;
}
/*********************popular_end****************/

/*********************play****************/
.play_m {
  background-color: rgba(0, 0, 0, 0.8);
  padding-top: 50px;
  padding-bottom: 50px;
}
#play {
  /* background-image: url(../img/30.jpg); */
  background-position: center;
}
.play1r {
  height: 450px;
  overflow-y: scroll;
}

/*********************play_end****************/

/*********************stream****************/
#stream .trend_2im2 {
  padding: 50px 15px 0px 15px !important;
  background-color: rgba(0, 0, 0, 0.8);
  height: 100%;
}
#stream .carousel-indicators {
  bottom: -50px;
}
#stream {
  border-top: 2px solid #de1002;
}
/*********************stream_end****************/

@media screen and (max-width: 767px) {
  .center_home .carousel-caption {
    padding: 10px;
    text-align: center;
  }
  .center_home .carousel-caption p {
    width: 100%;
    text-align: left;
  }

  .center_home img {
    min-height: 350px;
  }
  .center_home .font_60 {
    font-size: 24px;
  }
  .center_home h6 {
    font-size: 14px;
    line-height: 2em;
  }
  .center_home p {
    font-size: 14px;
  }
  .trend_2im {
    margin-top: 15px;
  }
  .trend_2ilast {
    text-align: center;
  }
  .popular_1 .nav-tabs li {
    margin-bottom: 5px;
  }
  .popular_2i1lm1 img {
    max-height: 240px;
  }
  .popular_2i1r {
    margin-top: 15px;
    text-align: center;
  }
  .popular_2i1r p {
    text-align: left;
  }
  .popular_2i1 {
    margin-bottom: 15px;
  }
  #choice img {
    min-height: 240px;
  }
  .play1l img {
    height: auto;
  }
  .play1r img {
    height: auto;
  }
  .play2l img {
    height: auto;
  }
  .play2r h5 {
    text-align: center;
  }
  .play2rir {
    margin-top: 15px;
  }
}

@media (min-width: 576px) and (max-width: 767px) {
  .trend_1l {
    text-align: left;
  }
  .trend_1r {
    text-align: right !important;
    margin-top: 0;
  }
  #popular .trend_1l {
    text-align: center;
  }
  .popular_2i1r {
    text-align: left;
    margin-top: 0;
  }
  #play .trend_1l {
    text-align: center;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .center_home img {
    min-height: 600px;
  }
  .carousel-caption {
    padding: 50px 100px;
  }
  .carousel-caption p {
    width: 60%;
  }
  .trend_2im1 img {
    min-height: 200px;
  }
  #choice .trend_2im1 img {
    min-height: 240px;
  }
  .play2r {
    padding: 10px !important;
    min-height: 515px;
  }
}

@media (min-width: 992px) and (max-width: 1200px) {
  .center_home img {
    min-height: 600px;
  }
  .carousel-caption {
    padding: 50px 100px;
  }
  .trend_2im1 img {
    min-height: 200px;
  }
  #choice .trend_2im1 img {
    min-height: 240px;
  }
  .play2r {
    padding: 10px !important;
    min-height: 515px;
  }
}
@media (min-width: 1201px) and (max-width: 1255px) {
}
</style>
