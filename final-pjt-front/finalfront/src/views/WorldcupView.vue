<template>
  <div v-if="!isDone">
    <h1 v-if="round === 2" class="text-center">결승</h1>
    <h1 v-else class="text-center">{{ round }} 강</h1>
    <div class="d-flex justify-content-center align-items-center">
      <div class="d-flex flex-column align-items-center" @click="selectPrev">
        <figure class="effect-jazz">
          <img :src="imgBaseUrlMain + getContestants[0]?.poster_path" alt="" />
        </figure>
        <h2>{{ getContestants[0]?.title }}</h2>
      </div>
      <h3 class="me-5 ms-5 col_red">VS</h3>
      <div class="d-flex flex-column align-items-center" @click="selectNext">
        <figure class="effect-jazz">
          <img :src="imgBaseUrlMain + getContestants[1]?.poster_path" alt="" />
        </figure>
        <h2>{{ getContestants[1]?.title }}</h2>
      </div>
    </div>
  </div>
  <div v-else>
    <h1 class="text-center">우승</h1>
    <div class="text-center">
      <figure>
        <img
          :src="
            'https://image.tmdb.org/t/p/w300/' + getContestants[0]?.poster_path
          "
          alt=""
        />
        <h4>{{ getContestants[0]?.title }}</h4>
      </figure>

      <p class="text-center mt-5">다음 영화가 내 취향에 반영됩니다</p>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters, mapMutations } from 'vuex';
import flowerAnimation from '@/util/flowerAnimation';
export default {
  name: 'VersusGameView',
  components: {},
  data() {
    return {
      winnerList: [],
      isDone: false,
      imgBaseUrlMain: 'https://image.tmdb.org/t/p/w500/',
      round: 8,
    };
  },
  computed: {
    ...mapGetters(['getContestants']),
  },

  methods: {
    ...mapActions(['getRandContestants', 'sendGameResult']),
    ...mapMutations(['SET_CONTESTANTS']),
    selectPrev() {
      this.winnerList.push(this.getContestants[0]);
      this.SET_CONTESTANTS(this.getContestants.slice(2));

      if (this.getContestants.length === 0) {
        this.SET_CONTESTANTS([...this.winnerList]);
        this.winnerList = [];
        this.round /= 2;
        if (this.getContestants.length === 1) {
          this.isDone = true;
          this.sendGameResult(this.getContestants);
          this.displayWinner();
        }
      }
    },
    selectNext() {
      this.winnerList.push(this.getContestants[1]);
      this.SET_CONTESTANTS(this.getContestants.slice(2));

      if (this.getContestants.length === 0) {
        this.SET_CONTESTANTS([...this.winnerList]);
        this.winnerList = [];
        this.round /= 2;
        if (this.getContestants.length === 1) {
          this.isDone = true;
          this.sendGameResult(this.getContestants);
          this.displayWinner();
        }
      }
    },
    displayWinner() {
      console.log('winners', this.winnerList);
      const animation = flowerAnimation();
      animation.startConfetti();

      setTimeout(() => {
        animation.stopConfetti();
      }, 3000);
    },
  },
  created() {
    this.getRandContestants(8);
  },
};
</script>

<style></style>
