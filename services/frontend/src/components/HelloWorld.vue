<template>
  <div id="app">
      {{msg}}
  <input v-model="msg"> 
  <button @click="getTable">getTable</button>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      msg: '',
    };
  },
  methods: {
    getTable() {
      axios.get('/',)
        .then((res) => {
          this.msg = res.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
};
</script>