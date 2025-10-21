<template>
  
<Home />

</template>

<script>

import Home from '@/views/Home.vue'

export default {
  name: 'App',
  components: {
    Home
  }
};
</script>

<style scoped>
*{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Poppins', sans-serif;
}

  .app {
    display: flex;
    flex-direction: column;
    min-height: 100vh;
  }



</style>
