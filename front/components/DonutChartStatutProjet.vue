<template>
  <DonutChart :options="options" :series="status_data" />
</template>
<script>

import {mapState} from 'vuex'

export default {


  data() {
    return {
      options: {
        labels: ['En cours', 'Términé'],
      },
    }
  },
  
  computed:{
      ...mapState('project', {
        status_data: state => state.status_data,
        errors: state => state.errors,
      })
  },
}
</script>
