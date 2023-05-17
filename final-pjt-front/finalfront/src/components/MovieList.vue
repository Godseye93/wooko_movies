<template>
  <section id="trend" class="pt-4 pb-5">
    <div class="container">
      <div class="row trend_1">
        <div class="col-md-6 col-6">
          <div class="trend_1l">
            <h4 class="mb-0">
              <i class="fa fa-youtube-play align-middle col_red me-1"></i>
              {{ category }} <span class="col_red">Movies</span>
            </h4>
          </div>
        </div>
      </div>
      <div class="row trend_2 mt-4">
        <div
          id="carouselExampleCaptions1"
          class="carousel slide"
          data-bs-ride="carousel"
        >
          <div class="carousel-indicators">
            <button
              type="button"
              data-bs-target="#carouselExampleCaptions1"
              data-bs-slide-to="0"
              class="active"
              aria-label="Slide 1"
            ></button>
            <button
              type="button"
              data-bs-target="#carouselExampleCaptions1"
              data-bs-slide-to="1"
              aria-label="Slide 2"
              class=""
              aria-current="true"
            ></button>
          </div>
          <div class="carousel-inner">
            <div class="carousel-item active">
              <div class="trend_2i row">
                <MovieItem />
                <MovieItem />
                <MovieItem />
                <MovieItem />
              </div>
            </div>
            <div class="carousel-item">
              <div class="trend_2i row">
                <MovieItem />
                <MovieItem />
                <MovieItem />
                <MovieItem />
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import MovieItem from './MovieItem.vue';
export default {
  name: 'MovieList',
  components: {
    MovieItem,
  },
  props: {
    category: {
      type: String,
      required: true,
    },
  },
};
</script>

<style></style>
