<template>
  <div class="home">
    <index msg="Welcome to Your Vue.js App"/>
  </div>
</template>

<script>
// @ is an alias to /src
import index from '@/components/index.vue'

export default {
  name: 'Home',
  components: {
    index
  }
}
</script>
