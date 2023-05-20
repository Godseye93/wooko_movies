<template>
  <div class="play2 row mt-4 profile-detail">
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
    <div class="col-md-8 p-0 me-0">
      <div class="play2r bg_grey p-4">
        <h3 class="mt-3">{{ getProfileInfo.username }} 님의 프로필</h3>
        <hr class="line border-0" />
        <!-- TODO 팔로우 구현시 이부분 수정, 선호장르 수정 -->
        <p class="mt-3">팔로워: 0</p>
        <p class="mt-3">팔로잉: 0</p>
        <p class="mt-3">선호장르 :</p>
        <ul class="mb-0 mt-1">
          <li class="d-inline-block">
            <a class="d-block">Analyze</a>
          </li>
          <li class="d-inline-block">
            <a class="d-block">Audio</a>
          </li>
          <li class="d-inline-block">
            <a class="d-block">Blog</a>
          </li>
        </ul>

        <div class="play2ri row mt-4">
          <div class="col-md-6">
            <div class="play2ril">
              <h6 class="fw-normal mb-3">
                <span> E-mail</span>
                <input
                  type="email"
                  id="email"
                  class="form-control bg-transparent"
                  placeholder="email"
                  v-model="profileInfo.email"
                />
              </h6>
              <h6 class="fw-normal mb-5">
                <span> 성별</span>
                <div class="row mt-3">
                  <div class="col-auto">
                    <div class="form-check">
                      <input
                        type="radio"
                        class="form-check-input"
                        id="male"
                        name="gender"
                        value="male"
                        v-model="profileInfo.sex"
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
                        v-model="profileInfo.sex"
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
              </h6>
              <button
                class="button mt-5"
                v-if="getCurUser.pk === getProfileInfo.id"
                @click="updateProfile(profileInfo)"
              >
                Submit
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex';
export default {
  name: 'ProfileUpdateView',
  data() {
    return {
      profileInfo: {
        email: null,
        sex: null,
      },
    };
  },
  computed: {
    ...mapGetters(['getProfileInfo', 'getCurUser']),
  },
  methods: {
    ...mapActions(['fetchProfileDetail', 'updateProfile']),
  },
  created() {
    this.fetchProfileDetail(this.getCurUser.pk);
    this.profileInfo.email = this.getProfileInfo.email;
    this.profileInfo.sex = this.getProfileInfo.sex;
  },
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
.profile-detail {
  max-width: 100vw;
  margin: 0px;
}
</style>
