<template>
<div>
 <!--  {{bailleurs_label}} -->
  <DonutChart :options="options" :series="bailleurs_count" />
</div>
</template>
<script>

import {mapState} from 'vuex'


export default {
  data() {
    return {
      options: {
       // labels: this.bailleurs_label,
       labels: ['Términé', 'En cours'],
      },
    }
  },

   computed:{
      ...mapState('bailleur', {
        bailleurs_count: state => state.bailleurs_count,
        bailleurs_label: state => state.bailleurs_label,
        errors: state => state.errors,
      })
  },
}
</script>
