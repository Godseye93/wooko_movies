<template>
  <section id="trend" class="pt-4 pb-5">
    <div class="container">
      <div class="row trend_1">
        <div class="col-md-6 col-6">
          <div class="trend_1l">
            <h4 class="mb-0">
              {{ category }} <span class="col_red">Movies</span>
            </h4>
          </div>
        </div>
      </div>
      <div class="row trend_2 mt-4">
        <div :id="slideId" class="carousel slide" data-bs-ride="carousel">
          <div class="carousel-indicators">
            <button
              type="button"
              :data-bs-target="`#${slideId}`"
              data-bs-slide-to="0"
              class="active"
              aria-label="Slide 1"
            ></button>
            <button
              type="button"
              :data-bs-target="`#${slideId}`"
              data-bs-slide-to="1"
              aria-label="Slide 2"
              class=""
              aria-current="true"
            ></button>
          </div>
          <div class="carousel-inner">
            <div class="carousel-item active">
              <div class="trend_2i row">
                <MovieItem
                  v-for="(item, index) in movieInfoList.slice(0, 4)"
                  :key="index"
                  :movie-info="item"
                />
              </div>
            </div>
            <div class="carousel-item">
              <div class="trend_2i row">
                <MovieItem
                  v-for="(item, index) in movieInfoList.slice(4, 8)"
                  :key="index"
                  :movieInfo="item"
                />
              </div>
            </div>
          </div>
          <button
            class="carousel-control-prev"
            type="button"
            :data-bs-target="`#${slideId}`"
            data-bs-slide="prev"
            style="left: -130px"
          >
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Previous</span>
          </button>
          <button
            class="carousel-control-next"
            type="button"
            :data-bs-target="`#${slideId}`"
            data-bs-slide="next"
            style="right: -130px"
          >
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Next</span>
          </button>
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
    movieInfoList: {
      type: Array,
      required: true,
    },
    slideId: {
      type: String,
      required: true,
    },
  },
};
</script>

<style></style>
