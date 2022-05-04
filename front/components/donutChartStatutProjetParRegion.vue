<template>
<div>
    <DonutChart :options="options" :series="project_status" />
</div>
</template>
<script>

import {mapState} from 'vuex'

export default {

  data() {
    return {
      options: {
        labels: ['Términé', 'En cours'],
      },
    }
  },

   computed:{
      ...mapState('region', {
        project_status: state => state.project_status,
        errors: state => state.errors,
      })
  },
  
}
</script>

