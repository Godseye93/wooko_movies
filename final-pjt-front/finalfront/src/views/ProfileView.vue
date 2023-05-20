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
        <h3 class="mt-3">{{getProfileInfo.username}} 님의 프로필</h3>
        <hr class="line border-0" />
        <!-- TODO 팔로우 구현시 이부분 수정, 선호장르 수정 -->
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
              <h6 class="fw-normal mb-3">
                E-mail : <span class="pull-right">{{getProfileInfo.email || '아직 등록한 이메일이 없습니다.'}}</span>
              </h6>
              <h6 class="fw-normal mb-5">
                성별 : <span class="pull-right">{{getProfileInfo.sex || '아직 성별을 등록하지 않았습니다.'}}</span>
              </h6>
              <router-link class="button mt-5"  :to="{name:'profile-update'}" v-if="getCurUser.pk===getProfileInfo.id" >프로필 수정하러 가기</router-link>
            </div>
          </div>
          
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
export default {
  name:'ProfileView',
  computed:{
    ...mapGetters(['getProfileInfo', 'getCurUser'])
  },
  methods:{
    ...mapActions(['fetchProfileDetail']),
    
  },
  created(){
    this.fetchProfileDetail(this.$route.params.userId)
  }
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
.profile-detail{
  max-width: 100vw;
  margin: 0px;
}
</style>
