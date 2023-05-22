<template>
  <div>
    <div @click="selectPrev">{{ getContestants[0]?.title }}</div>
    <div @click="selectNext">{{ getContestants[1]?.title }}</div>
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
    };
  },
  computed: {
    ...mapGetters(['getContestants']),
  },
  methods: {
    ...mapActions(['getRandContestants']),
    ...mapMutations(['SET_CONTESTANTS']),
    selectPrev() {
      console.log('select1');
      this.winnerList.push(this.getContestants[0]);
      this.SET_CONTESTANTS(this.getContestants.slice(2));
      if (this.getContestants.length === 0) {
        this.displayWinner();
      }
    },
    selectNext() {
      console.log('select2');
      this.winnerList.push(this.getContestants[1]);
      this.SET_CONTESTANTS(this.getContestants.slice(2));
      if (this.getContestants.length === 0) {
        this.displayWinner();
      }
    },
    displayWinner() {
      console.log('winners', this.winnerList);
    },
  },
  created() {
    this.getRandContestants(8);
  },
};
</script>

<style></style>
