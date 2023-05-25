<template>
  <div class="d-flex justify-content-center align-items-center" v-if="!isDone">
    <div class="d-flex flex-column align-items-center" @click="selectPrev">
      <figure class="effect-jazz">
        <img
          v-if="getContestants[0]"
          :src="imgBaseUrlMain + getContestants[0].profile_path"
          alt=""
        />
      </figure>
      <h2>{{ getContestants[0]?.name }}</h2>
    </div>
    <h3 class="me-5 ms-5 col_red">VS</h3>
    <div class="d-flex flex-column align-items-center" @click="selectNext">
      <figure class="effect-jazz">
        <img
          v-if="getContestants[1]"
          :src="imgBaseUrlMain + getContestants[1].profile_path"
          alt=""
        />
      </figure>
      <h2>{{ getContestants[1]?.name }}</h2>
    </div>
  </div>
  <div v-else>
    <div class="d-flex justify-content-center">
      <figure v-for="(item, index) in winnerList" :key="index" class="me-5">
        <img
          :src="'https://image.tmdb.org/t/p/w300/' + item.profile_path"
          alt=""
        />
        <h4>{{ item.name }}</h4>
      </figure>
    </div>
    <p class="text-center mt-5">다음 감독들이 내 취향에 반영됩니다</p>
  </div>
</template>

<script>
import { mapActions, mapGetters, mapMutations } from 'vuex';
export default {
  name: 'VersusGameDirectorView',
  components: {},
  data() {
    return {
      winnerList: [],
      imgBaseUrlMain: 'https://image.tmdb.org/t/p/w500/',
      isDone: false,
    };
  },
  computed: {
    ...mapGetters(['getContestants']),
  },
  methods: {
    ...mapActions(['getRandDirectors', 'sendGameResult']),
    ...mapMutations(['SET_CONTESTANTS']),
    selectPrev() {
      console.log('select1');
      this.winnerList.push(this.getContestants[0]);
      this.SET_CONTESTANTS(this.getContestants.slice(2));
      if (this.getContestants.length === 0) {
        this.isDone = true;
        this.sendGameResult(this.winnerList);
      }
    },
    selectNext() {
      console.log('select2');
      this.winnerList.push(this.getContestants[1]);
      this.SET_CONTESTANTS(this.getContestants.slice(2));
      if (this.getContestants.length === 0) {
        this.isDone = true;
        this.sendGameResult(this.winnerList);
      }
    },
  },
  created() {
    this.getRandDirectors(8);
  },
};
</script>

<style>
.effect-jazz {
  cursor: pointer;
}
</style>
