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
        <p class="mt-3">팔로워: {{ getProfileInfo.followers_count }}</p>
        <div
          v-if="getCurUser.pk !== getProfileInfo.id"
          @click="followToggle(getProfileInfo.id)"
        >
          <button class="border-0 rounded" id="follow-btn" v-if="!isFollowed">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="24"
              height="24"
              fill="currentColor"
              class="bi bi-person-fill-add me-2"
              viewBox="0 0 16 16"
            >
              <path
                d="M12.5 16a3.5 3.5 0 1 0 0-7 3.5 3.5 0 0 0 0 7Zm.5-5v1h1a.5.5 0 0 1 0 1h-1v1a.5.5 0 0 1-1 0v-1h-1a.5.5 0 0 1 0-1h1v-1a.5.5 0 0 1 1 0Zm-2-6a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z"
              />
              <path
                d="M2 13c0 1 1 1 1 1h5.256A4.493 4.493 0 0 1 8 12.5a4.49 4.49 0 0 1 1.544-3.393C9.077 9.038 8.564 9 8 9c-5 0-6 3-6 4Z"
              />
            </svg>

            <span>팔로우</span>
          </button>

          <button class="button rounded" v-else>
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="24"
              height="24"
              fill="currentColor"
              class="bi bi-person-fill-dash me-2"
              viewBox="0 0 16 16"
            >
              <path
                d="M12.5 16a3.5 3.5 0 1 0 0-7 3.5 3.5 0 0 0 0 7ZM11 12h3a.5.5 0 0 1 0 1h-3a.5.5 0 0 1 0-1Zm0-7a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z"
              />
              <path
                d="M2 13c0 1 1 1 1 1h5.256A4.493 4.493 0 0 1 8 12.5a4.49 4.49 0 0 1 1.544-3.393C9.077 9.038 8.564 9 8 9c-5 0-6 3-6 4Z"
              />
            </svg>

            <span>팔로우 해제</span>
          </button>
        </div>

        <p class="mt-3">팔로잉: {{ getProfileInfo.followings_count }}</p>
        <p class="mt-3">선호장르</p>
        <ul class="mb-0 mt-1">
          <li
            class="d-inline-block"
            v-for="(item, index) in getProfileInfo.liked_genres"
            :key="index"
          >
            <a class="d-block">{{ item.name }}</a>
          </li>
        </ul>

        <div class="play2ri row mt-4">
          <div class="col-md-6">
            <div class="play2ril">
              <h6 class="fw-normal mb-3">
                E-mail :
                <span class="pull-right">{{
                  getProfileInfo.email || '아직 등록한 이메일이 없습니다.'
                }}</span>
              </h6>
              <h6 class="fw-normal mb-5">
                성별 :
                <span class="pull-right">{{
                  getProfileInfo.sex || '아직 성별을 등록하지 않았습니다.'
                }}</span>
              </h6>
            </div>
            <router-link
              class="button mt-0 me-3"
              :to="{ name: 'profile-update' }"
              v-if="getCurUser.pk === getProfileInfo.id"
              >프로필 수정하기</router-link
            >
            <router-link
              class="button mt-3 me-3"
              :to="{ name: 'change-passwd' }"
              v-if="getCurUser.pk === getProfileInfo.id"
              >비밀번호 변경하기</router-link
            >
            <button
              class="button mt-3 bg-warning rounded col_light text-dark"
              v-if="getCurUser.pk === getProfileInfo.id"
              @click="delUser"
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="24"
                height="24"
                fill="currentColor"
                class="bi bi-person-x me-2"
                viewBox="0 0 16 16"
              >
                <path
                  d="M11 5a3 3 0 1 1-6 0 3 3 0 0 1 6 0ZM8 7a2 2 0 1 0 0-4 2 2 0 0 0 0 4Zm.256 7a4.474 4.474 0 0 1-.229-1.004H3c.001-.246.154-.986.832-1.664C4.484 10.68 5.711 10 8 10c.26 0 .507.009.74.025.226-.341.496-.65.804-.918C9.077 9.038 8.564 9 8 9c-5 0-6 3-6 4s1 1 1 1h5.256Z"
                />
                <path
                  d="M12.5 16a3.5 3.5 0 1 0 0-7 3.5 3.5 0 0 0 0 7Zm-.646-4.854.646.647.646-.647a.5.5 0 0 1 .708.708l-.647.646.647.646a.5.5 0 0 1-.708.708l-.646-.647-.646.647a.5.5 0 0 1-.708-.708l.647-.646-.647-.646a.5.5 0 0 1 .708-.708Z"
                />
              </svg>

              <span>회원 탈퇴하기</span>
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex';
export default {
  name: 'ProfileView',
  computed: {
    ...mapGetters(['getProfileInfo', 'getCurUser']),
    isFollowed() {
      return this.getProfileInfo.followers_list?.some(
        (follower) => follower.id === this.getCurUser.pk,
      );
    },
  },
  methods: {
    ...mapActions(['fetchProfileDetail', 'delUser', 'followToggle']),
  },
  created() {
    this.fetchProfileDetail(this.$route.params.userId);
  },
  beforeRouteUpdate(to, from, next) {
    this.fetchProfileDetail(to.params.userId);
    next(); // URL 이동, 라우팅 하기
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

#follow-btn {
  --bs-text-opacity: 1;
  color: rgba(var(--bs-white-rgb), var(--bs-text-opacity));
  --bs-bg-opacity: 1;
  background-color: rgba(var(--bs-success-rgb), var(--bs-bg-opacity));
  padding: 10px 20px;
  display: inline-block;
}
#follow-btn:hover {
  background-color: #fff;
  color: #28a745;
  transition: 0.3s;
}
</style>
