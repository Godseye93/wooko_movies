<template>
  <div class="col-md-3 col-6">
    <div class="trend_2im clearfix position-relative">
      <div class="trend_2im1 clearfix">
        <div class="grid">
          <figure class="effect-jazz mb-0">
            <router-link :to="{ name: 'movie-detail' }"
              ><img src="../assets/logo.png" class="w-100" alt="img25"
            /></router-link>
          </figure>
        </div>
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
      <h5><a class="col_red" href="#">Semper</a></h5>
      <p class="mb-2">
        A father travels from Oklahoma to France to help his...
      </p>
      <span class="col_red">
        <i class="fa fa-star"></i>
        <i class="fa fa-star"></i>
        <i class="fa fa-star"></i>
        <i class="fa fa-star"></i>
        <i class="fa fa-star"></i>
      </span>
      <p class="mb-0">1 Views</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MovieItem',
};
</script>

<style></style>
