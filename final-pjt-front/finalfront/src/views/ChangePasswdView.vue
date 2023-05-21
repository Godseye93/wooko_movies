<template>
  <div class="ms-5 mt-5">
    <h2 class="col_red mb-4">비밀번호 변경</h2>
    <p>변경할 비밀번호를 입력하세요</p>
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
        v-model="new_password1"
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
        v-model="new_password2"
      />
    </div>
    <p v-if="isPasswordSame" class="mt-3 text-success">비밀번호가 일치합니다</p>
    <p v-else class="mt-3 text-warning">비밀번호가 일치하지 않습니다</p>
    <button
      class="button"
      @click="fetchChangePasswd({ new_password1, new_password2 })"
    >
      비밀번호 변경 하기
    </button>
  </div>
</template>

<script>
import { mapActions } from 'vuex';
export default {
  name: 'ChangePasswdView',
  data() {
    return {
      new_password1: '',
      new_password2: '',
    };
  },
  computed: {
    isPasswordSame() {
      return this.new_password1 === this.new_password2;
    },
  },
  methods: {
    ...mapActions(['fetchChangePasswd']),
  },
};
</script>

<style></style>
