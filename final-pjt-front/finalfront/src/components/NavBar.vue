<template>
  <section id="nav-bar">
    <section id="top">
      <div class="container">
        <div class="row top_1">
          <div class="col-md-3">
            <div class="top_1l pt-1">
              <h3 class="mb-0">
                <router-link
                  :to="{ name: HomeView }"
                  style="text-decoration: none; color: var(--bs-red)"
                  ><i class="fa fa-video-camera col_red me-1"></i>WOOKO
                  MOVIES</router-link
                >
              </h3>
            </div>
          </div>
          <div class="col-md-5">
            <div class="top_1m">
              <div class="input-group">
                <input
                  type="text"
                  class="form-control bg-black"
                  placeholder="Search Site..."
                />
                <span class="input-group-btn">
                  <button
                    class="btn text-white rounded-0 bg-danger"
                    type="button"
                  >
                    Search
                  </button>
                </span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section id="header">
      <nav class="navbar navbar-expand-md navbar-light" id="navbar_sticky">
        <div class="container">
          <button
            class="navbar-toggler"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#navbarSupportedContent"
            aria-controls="navbarSupportedContent"
            aria-expanded="false"
            aria-label="Toggle navigation"
          >
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav mb-0">
              <li class="nav-item">
                <router-link class="nav-link" to="/"
                  >내 취향 영화 고르기</router-link
                >
              </li>
              <li class="nav-item">
                <router-link class="nav-link" to="/">이상형 월드컵</router-link>
              </li>
              <li class="nav-item">
                <router-link class="nav-link" to="/">추천 기능</router-link>
              </li>
            </ul>
          </div>
        </div>
      </nav>
    </section>
  </section>
</template>

<script>
export default {
  name: 'NavBar',
};
</script>

<style></style>
