<template>
  <div class="blog_1r1 p-4 mt-4">
    <h4>Login <span class="col_red">Form</span></h4>
    <hr class="line mb-4" />
    <div class="input-group input-group-merge">
      <div
        class="input-group-text bg-transparent text-white border-right-0"
        data-password="false"
      >
        <span class="fa fa-user"></span>
      </div>
      <input
        type="username"
        id="username"
        class="form-control bg-transparent"
        placeholder="Username"
      />
    </div>
    <div class="input-group input-group-merge mt-3">
      <div
        class="input-group-text bg-transparent text-white border-right-0"
        data-password="false"
      >
        <span class="fa fa-user"></span>
      </div>
      <input
        type="password"
        id="username"
        class="form-control bg-transparent"
        placeholder="password"
      />
    </div>
    <div class="form-check mt-3">
      <input type="checkbox" class="form-check-input" id="checkmeout0" />
      <label class="form-check-label" for="checkmeout0">Remember Me</label>
    </div>
    <h6 class="mt-3">
      <a class="button" href="blog_detail.html"
        ><i class="fa fa-long-arrow-right align-middle me-1"></i> Login</a
      >
    </h6>
    <h6 class="mt-3">
      <a class="col_red" href="blog_detail.html"
        >Create an account <i class="fa fa-long-arrow-right ms-1"></i
      ></a>
    </h6>
    <h6 class="mt-3">
      <a class="col_red" href="blog_detail.html">Forgot your username? </a>
    </h6>
    <h6 class="mt-3 mb-0">
      <a class="col_red" href="blog_detail.html">Forgot your password? </a>
    </h6>
  </div>
</template>

<script>
export default {
  name: 'LoginView',
};
</script>

<style></style>
