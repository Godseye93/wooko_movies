<template>
  <div class="blog_1r1 p-4 mt-4">
    <h4>Login <span class="col_red">Form</span></h4>
    <hr class="mb-4" />
    <div class="input-group input-group-merge">
      <div
        class="input-group-text bg-transparent text-white border-right-0"
        data-password="false"
      >
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="16"
          height="16"
          fill="currentColor"
          class="bi bi-person"
          viewBox="0 0 16 16"
        >
          <path
            d="M8 8a3 3 0 1 0 0-6 3 3 0 0 0 0 6Zm2-3a2 2 0 1 1-4 0 2 2 0 0 1 4 0Zm4 8c0 1-1 1-1 1H3s-1 0-1-1 1-4 6-4 6 3 6 4Zm-1-.004c-.001-.246-.154-.986-.832-1.664C11.516 10.68 10.289 10 8 10c-2.29 0-3.516.68-4.168 1.332-.678.678-.83 1.418-.832 1.664h10Z"
          />
        </svg>
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
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="16"
          height="16"
          fill="currentColor"
          class="bi bi-person"
          viewBox="0 0 16 16"
        >
          <path
            d="M8 8a3 3 0 1 0 0-6 3 3 0 0 0 0 6Zm2-3a2 2 0 1 1-4 0 2 2 0 0 1 4 0Zm4 8c0 1-1 1-1 1H3s-1 0-1-1 1-4 6-4 6 3 6 4Zm-1-.004c-.001-.246-.154-.986-.832-1.664C11.516 10.68 10.289 10 8 10c-2.29 0-3.516.68-4.168 1.332-.678.678-.83 1.418-.832 1.664h10Z"
          />
        </svg>
      </div>
      <input
        type="password"
        id="username"
        class="form-control bg-transparent"
        placeholder="password"
      />
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
  </div>
</template>

<script>
export default {
  name: 'LoginView',
};
</script>

<style></style>
