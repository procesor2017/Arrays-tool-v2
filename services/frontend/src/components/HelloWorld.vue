<template>
  <div id="app">
      {{msg}}
    <input v-model="myInput"> 
    <button @click="getTable">getTable</button>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      msg: '',
      myInput: "",
    };
  },
  methods: {
    getTable() {
      let payload = {
        "data": [{"0":"a","1":"aa","2":"aaa","3":"aaaa","4":"aaaaa"},{"0":"b","1":"bb","2":"bbb","3":"bbbb","4":"bbbbb"},{"4":"ccccc"},{"4":"ddddd"}]
      }

      axios.post('/getInformation', payload)
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