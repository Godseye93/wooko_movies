<template>
  <div id="app">
    <NavBar />
    <router-view />
    <br /><br /><br />
    <FooterComponent />
  </div>
</template>

<script>
import NavBar from '@/components/NavBar.vue';
import FooterComponent from '@/components/FooterComponent.vue';
export default {
  name: 'App',
  components: {
    NavBar,
    FooterComponent,
  },
};
</script>

<style></style>
