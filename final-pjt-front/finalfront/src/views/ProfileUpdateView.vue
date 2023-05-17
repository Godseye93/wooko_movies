<template>
  <div class="play2 row mt-4">
    <div class="col-md-4 p-0">
      <div class="play2l">
        <div class="grid clearfix">
          <figure class="effect-jazz mb-0">
            <a href="#"
              ><img
                src="../assets/logo.png"
                height="515"
                class="w-100"
                alt="abc"
            /></a>
          </figure>
        </div>
      </div>
    </div>
    <div class="col-md-8 p-0">
      <div class="play2r bg_grey p-4">
        <h3 class="mt-3">xx님의 프로필</h3>
        <hr class="line border-0" />
        <p class="mt-3">팔로워: 0</p>
        <p class="mt-3">팔로잉: 0</p>
        <p class="mt-3">선호장르 : <ul class="mb-0 mt-1">
                <li class="d-inline-block">
                  <a class="d-block">Analyze</a>
                </li>
                <li class="d-inline-block">
                  <a class="d-block">Audio</a>
                </li>
                <li class="d-inline-block">
                  <a class="d-block">Blog</a>
                </li>
              </ul></p>
        <div class="play2ri row mt-4">
          <div class="col-md-6">
            <div class="play2ril">
              <h6 class="fw-normal">
                Running Time: <span class="pull-right">1 hr 50 min</span>
              </h6>
              <hr class="hr_1" />
              <h6 class="fw-normal">
                Genre: <span class="pull-right">Action, Thriller</span>
              </h6>
              <hr class="hr_1" />
              <h6 class="fw-normal">
                Director: <span class="pull-right">Eget Nulla</span>
              </h6>
              <hr class="hr_1" />
       
            </div>
          </div>
          <div class="col-md-6">
            <div class="play2rir">
              <h6 class="fw-normal">Imdb - 9.2</h6>
              <div class="progress">
                <div
                  class="progress-bar"
                  role="progressbar"
                  style="width: 92%"
                  aria-valuenow="25"
                  aria-valuemin="0"
                  aria-valuemax="100"
                ></div>
              </div>
              <h6 class="fw-normal mt-3">Semper - 7.3</h6>
              <div class="progress">
                <div
                  class="progress-bar"
                  role="progressbar"
                  style="width: 73%"
                  aria-valuenow="25"
                  aria-valuemin="0"
                  aria-valuemax="100"
                ></div>
              </div>
              <h6 class="fw-normal mt-3">Dapibus - 9.0</h6>
              <div class="progress">
                <div
                  class="progress-bar"
                  role="progressbar"
                  style="width: 90%"
                  aria-valuenow="25"
                  aria-valuemin="0"
                  aria-valuemax="100"
                ></div>
              </div>
              <h6 class="fw-normal mt-3">Ipsum - 8.3</h6>
              <div class="progress">
                <div
                  class="progress-bar"
                  role="progressbar"
                  style="width: 83%"
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
export default {
  name:'ProfileUpdateView'
};
</script>

<style scoped>
ul li a {
  font-size: 14px;
  padding: 7px 12px 6px;
  background: #252525;
  margin: 0px 2px 6px 0px;
  cursor: pointer;
}
</style>
