<template>
  <div v-if="!isDone">
    <div @click="selectPrev">{{ getContestants[0]?.title }}</div>
    <div @click="selectNext">{{ getContestants[1]?.title }}</div>
  </div>
  <div v-else>
    <div>Winner: {{ contestants[0]?.name }}</div>
  </div>
</template>

<script>
import { mapActions, mapGetters, mapMutations } from 'vuex';
export default {
  name: 'VersusGameView',
  components: {},
  data() {
    return {
      winnerList: [],
      isDone: false,
    };
  },
  computed: {
    ...mapGetters(['getContestants']),
  },

  methods: {
    ...mapActions(['getRandContestants']),
    ...mapMutations(['SET_CONTESTANTS']),
    selectPrev() {
      this.winnerList.push(this.getContestants[0]);
      this.SET_CONTESTANTS(this.getContestants.slice(2));

      if (this.getContestants.length === 0) {
        this.SET_CONTESTANTS([...this.winnerList]);
        this.winnerList = [];
        if (this.getContestants.length === 1) {
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
        if (this.getContestants.length === 1) {
          this.displayWinner();
        }
      }
    },
    displayWinner() {
      console.log('winners', this.winnerList);
      this.SET_CONTESTANTS([]);
      this.isDone = true;
    },
  },
  created() {
    this.getRandContestants(8);
  },
};
</script>

<style></style>
