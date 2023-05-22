<template>
  <div>
    <div @click="selectPrev">{{ curContestant[0]?.name }}</div>
    <div @click="selectNext">{{ curContestant[1]?.name }}</div>
  </div>
</template>

<script>
export default {
  name: 'VersusGameView',
  components: {},
  data() {
    return {
      contestants: [
        {
          name: 'movie3',
          poster_path:
            'https://image.tmdb.org/t/p/w500/8UlWHLMpgZm9bx6QYh0NFoq67TZ.jpg',
        },
        {
          name: 'movie4',
          poster_path:
            'https://image.tmdb.org/t/p/w500/9kg73Mg8WJKlB9Y2SAJzeDKAnuB.jpg',
        },
        {
          name: 'movie5',
          poster_path:
            'https://image.tmdb.org/t/p/w500/2lBOQK06tltt8SQaswgb8d657Mv',
        },
        {
          name: 'movie6',
          poster_path:
            'https://image.tmdb.org/t/p/w500/5NxjLfs7Bi07bfZCRl9CCnUw7AA.jpg',
        },
        {
          name: 'movie7',
          poster_path:
            'https://image.tmdb.org/t/p/w500/fX8e94MEWSuTJExndVYxKsmA4Hw.jpg',
        },
        {
          name: 'movie8',
          poster_path:
            'https://image.tmdb.org/t/p/w500/y95lQLnuNKdPAzw9F9Ab8kJ80c3.jpg',
        },
      ],
      curContestant: [
        {
          name: 'movie1',
          poster_path:
            'https://image.tmdb.org/t/p/w500/6KErczPBROQty7QoIsaa6wJYXZi.jpg',
        },
        {
          name: 'movie2',
          poster_path:
            'https://image.tmdb.org/t/p/w500/srYya1ZlI97Au4jUYAktDe3avyA.jpg',
        },
      ],
      winnerList: [],
    };
  },
  methods: {
    selectPrev() {
      console.log('select1');
      this.winnerList.push(this.curContestant[0]);
      this.curContestant = this.contestants.splice(0, 2);
      if (this.contestants.length === 0) {
        this.displayWinner();
      }
    },
    selectNext() {
      console.log('select2');
      this.winnerList.push(this.curContestant[1]);
      this.curContestant = this.contestants.splice(0, 2);
      if (this.contestants.length === 0) {
        this.displayWinner();
      }
    },
    displayWinner() {
      console.log('winners', this.winnerList);
    },
  },
  created() {
    // fetchMovieList();
  },
};
</script>

<style></style>
