<template>
  <div id="app" class="app">
    <!-- Aqui o Vue Router renderiza a página atual -->
    <router-view />
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style scoped>
* {
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