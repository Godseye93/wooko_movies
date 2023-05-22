<template>
  <div v-if="!isDone">
    <div @click="selectPrev">{{ contestants[0]?.name }}</div>
    <div @click="selectNext">{{ contestants[1]?.name }}</div>
  </div>
  <div v-else>
    <div>Winner: {{ contestants[0]?.name }}</div>
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
          name: 'movie1',
          poster_path:
            'https://image.tmdb.org/t/p/w500/6KErczPBROQty7QoIsaa6wJYXZi.jpg',
        },
        {
          name: 'movie2',
          poster_path:
            'https://image.tmdb.org/t/p/w500/srYya1ZlI97Au4jUYAktDe3avyA.jpg',
        },
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

      winnerList: [],
      isDone: false,
    };
  },

  methods: {
    selectPrev() {
      this.winnerList.push(this.contestants[0]);
      this.contestants.splice(0, 2);

      if (this.contestants.length === 0) {
        this.contestants = [...this.winnerList];
        this.winnerList = [];
        if (this.contestants.length === 1) {
          this.displayWinner();
        }
      }
    },
    selectNext() {
      this.winnerList.push(this.contestants[1]);
      this.contestants.splice(0, 2);

      if (this.contestants.length === 0) {
        this.contestants = [...this.winnerList];
        this.winnerList = [];
        if (this.contestants.length === 1) {
          this.displayWinner();
        }
      }
    },
    displayWinner() {
      console.log('winners', this.winnerList);
      this.isDone = true;
    },
  },
  created() {
    // fetchMovieList();
  },
};
</script>

<style></style>
