<template>
  <div class="blog_1r1 p-4 mt-4 w-50" style="margin: 0 auto">
    <h4>Signup <span class="col_red">Form</span></h4>
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
        v-model="userInfo.username"
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
          class="bi bi-key"
          viewBox="0 0 16 16"
        >
          <path
            d="M0 8a4 4 0 0 1 7.465-2H14a.5.5 0 0 1 .354.146l1.5 1.5a.5.5 0 0 1 0 .708l-1.5 1.5a.5.5 0 0 1-.708 0L13 9.207l-.646.647a.5.5 0 0 1-.708 0L11 9.207l-.646.647a.5.5 0 0 1-.708 0L9 9.207l-.646.647A.5.5 0 0 1 8 10h-.535A4 4 0 0 1 0 8zm4-3a3 3 0 1 0 2.712 4.285A.5.5 0 0 1 7.163 9h.63l.853-.854a.5.5 0 0 1 .708 0l.646.647.646-.647a.5.5 0 0 1 .708 0l.646.647.646-.647a.5.5 0 0 1 .708 0l.646.647.793-.793-1-1h-6.63a.5.5 0 0 1-.451-.285A3 3 0 0 0 4 5z"
          />
          <path d="M4 8a1 1 0 1 1-2 0 1 1 0 0 1 2 0z" />
        </svg>
      </div>
      <input
        type="password"
        id="password"
        class="form-control bg-transparent"
        placeholder="password"
        v-model="userInfo.password1"
      />
    </div>
    <div class="input-group input-group-merge mt-3">
      <div
        class="input-group-text bg-transparent text-white border-right-0"
        data-password="false"
      >
        <svg
          v-if="!isPasswordSame"
          xmlns="http://www.w3.org/2000/svg"
          width="16"
          height="16"
          fill="currentColor"
          class="bi bi-x-lg"
          viewBox="0 0 16 16"
        >
          <path
            d="M2.146 2.854a.5.5 0 1 1 .708-.708L8 7.293l5.146-5.147a.5.5 0 0 1 .708.708L8.707 8l5.147 5.146a.5.5 0 0 1-.708.708L8 8.707l-5.146 5.147a.5.5 0 0 1-.708-.708L7.293 8 2.146 2.854Z"
          />
        </svg>
        <svg
          v-else
          xmlns="http://www.w3.org/2000/svg"
          width="16"
          height="16"
          fill="currentColor"
          class="bi bi-check-lg"
          viewBox="0 0 16 16"
        >
          <path
            d="M12.736 3.97a.733.733 0 0 1 1.047 0c.286.289.29.756.01 1.05L7.88 12.01a.733.733 0 0 1-1.065.02L3.217 8.384a.757.757 0 0 1 0-1.06.733.733 0 0 1 1.047 0l3.052 3.093 5.4-6.425a.247.247 0 0 1 .02-.022Z"
          />
        </svg>
      </div>
      <input
        type="password"
        id="passwordCheck"
        class="form-control bg-transparent"
        placeholder="password check"
        v-model="userInfo.password2"
        @keyup.enter="fetchSignUp(userInfo)"
      />
    </div>
    <p v-if="isPasswordSame" class="mt-3 text-success">비밀번호가 일치합니다</p>
    <p v-else class="mt-3 text-warning">비밀번호가 일치하지 않습니다</p>
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
          class="bi bi-envelope-at"
          viewBox="0 0 16 16"
        >
          <path
            d="M2 2a2 2 0 0 0-2 2v8.01A2 2 0 0 0 2 14h5.5a.5.5 0 0 0 0-1H2a1 1 0 0 1-.966-.741l5.64-3.471L8 9.583l7-4.2V8.5a.5.5 0 0 0 1 0V4a2 2 0 0 0-2-2H2Zm3.708 6.208L1 11.105V5.383l4.708 2.825ZM1 4.217V4a1 1 0 0 1 1-1h12a1 1 0 0 1 1 1v.217l-7 4.2-7-4.2Z"
          />
          <path
            d="M14.247 14.269c1.01 0 1.587-.857 1.587-2.025v-.21C15.834 10.43 14.64 9 12.52 9h-.035C10.42 9 9 10.36 9 12.432v.214C9 14.82 10.438 16 12.358 16h.044c.594 0 1.018-.074 1.237-.175v-.73c-.245.11-.673.18-1.18.18h-.044c-1.334 0-2.571-.788-2.571-2.655v-.157c0-1.657 1.058-2.724 2.64-2.724h.04c1.535 0 2.484 1.05 2.484 2.326v.118c0 .975-.324 1.39-.639 1.39-.232 0-.41-.148-.41-.42v-2.19h-.906v.569h-.03c-.084-.298-.368-.63-.954-.63-.778 0-1.259.555-1.259 1.4v.528c0 .892.49 1.434 1.26 1.434.471 0 .896-.227 1.014-.643h.043c.118.42.617.648 1.12.648Zm-2.453-1.588v-.227c0-.546.227-.791.573-.791.297 0 .572.192.572.708v.367c0 .573-.253.744-.564.744-.354 0-.581-.215-.581-.8Z"
          />
        </svg>
      </div>
      <input
        type="email"
        id="email"
        class="form-control bg-transparent"
        placeholder="email"
        v-model="userInfo.email"
      />
    </div>
    <div class="row mt-3">
      <div class="col-auto">
        <div class="form-check">
          <input
            type="radio"
            class="form-check-input"
            id="male"
            name="gender"
            value="male"
            v-model="userInfo.sex"
          />
          <label class="form-check-label" for="male">
            남자
            <span>
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="16"
                height="16"
                fill="currentColor"
                class="bi bi-gender-male"
                viewBox="0 0 16 16"
              >
                <path
                  fill-rule="evenodd"
                  d="M9.5 2a.5.5 0 0 1 0-1h5a.5.5 0 0 1 .5.5v5a.5.5 0 0 1-1 0V2.707L9.871 6.836a5 5 0 1 1-.707-.707L13.293 2H9.5zM6 6a4 4 0 1 0 0 8 4 4 0 0 0 0-8z"
                />
              </svg>
            </span>
          </label>
        </div>
      </div>
      <div class="col-auto">
        <div class="form-check">
          <input
            type="radio"
            class="form-check-input"
            id="female"
            name="gender"
            value="female"
            v-model="userInfo.sex"
          />
          <label class="form-check-label" for="female">
            여자
            <span>
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="16"
                height="16"
                fill="currentColor"
                class="bi bi-gender-female"
                viewBox="0 0 16 16"
              >
                <path
                  fill-rule="evenodd"
                  d="M8 1a4 4 0 1 0 0 8 4 4 0 0 0 0-8zM3 5a5 5 0 1 1 5.5 4.975V12h2a.5.5 0 0 1 0 1h-2v2.5a.5.5 0 0 1-1 0V13h-2a.5.5 0 0 1 0-1h2V9.975A5 5 0 0 1 3 5z"
                />
              </svg>
            </span>
          </label>
        </div>
      </div>
    </div>
    <h6 class="mt-3">
      <button class="button border-0" @click="fetchSignUp(userInfo)">
        Sign Up
      </button>
    </h6>
    <h6 class="mt-3">
      <router-link :to="{ name: 'login' }" class="col_red"
        >계정이 이미 있으신가요? 로그인 하러 가기</router-link
      >
    </h6>
  </div>
</template>

<script>
import { mapActions } from 'vuex';
export default {
  name: 'SignupView',
  data() {
    return {
      userInfo: {
        username: null,
        password1: null,
        password2: null,
        email: null,
        sex: null,
      },
    };
  },
  computed: {
    isPasswordSame() {
      return this.userInfo.password1 === this.userInfo.password2;
    },
  },
  methods: {
    ...mapActions(['fetchSignUp']),
  },
};
</script>

<style>
.input-group-text {
  margin-right: 1px;
}
</style>
