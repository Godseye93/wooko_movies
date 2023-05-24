<template>
  <div class="d-flex justify-content-center align-items-center" v-if="!isDone">
    <div class="d-flex flex-column align-items-center" @click="selectPrev">
      <figure class="effect-jazz">
        <img
          v-if="getContestants"
          :src="imgBaseUrlMain + getContestants[0].poster_path"
          alt=""
        />
      </figure>
      <h2>{{ getContestants[0]?.title }}</h2>
    </div>
    <h3 class="me-5 ms-5 col_red">VS</h3>
    <div class="d-flex flex-column align-items-center" @click="selectNext">
      <figure class="effect-jazz">
        <img
          v-if="getContestants"
          :src="imgBaseUrlMain + getContestants[1].poster_path"
          alt=""
        />
      </figure>
      <h2>{{ getContestants[1]?.title }}</h2>
    </div>
  </div>
  <div v-else>
    <div class="d-flex justify-content-center">
      <figure v-for="(item, index) in winnerList" :key="index" class="me-5">
        <img
          :src="'https://image.tmdb.org/t/p/w300/' + item.poster_path"
          alt=""
        />
        <h4>{{ item.title }}</h4>
      </figure>
    </div>
    <p class="text-center mt-5">다음 영화들이 내 취향에 반영됩니다</p>
  </div>
</template>

<script>
import { mapActions, mapGetters, mapMutations } from 'vuex';
export default {
  name: 'VersusGameMovieView',
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
    ...mapActions(['getRandContestants', 'sendGameResult']),
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
    this.getRandContestants(8);
  },
};
</script>

<style>
.effect-jazz {
  cursor: pointer;
}
</style>
