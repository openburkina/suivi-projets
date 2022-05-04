<template>
<div>
 
  <LineChart :options="options" :series="series" />
</div>
</template>
<script>

import {mapState} from 'vuex'

export default {
  data() {
    return {
      options: {
        chart: {
          id: 'line-chart-montant-secteur',
        },
        xaxis: {
          categories: ['Sécurité', 'Santé', 'Éducation', 'Agriculture'],
        },
      },
      series: [
        {
          name: 'Sécurité',
          data: [10, 20, 30, 40],
        },
        {
          name: 'Santé',
          data: [15, 25, 35, 50],
        },
        {
          name: 'Éducation',
          data: [9, 7, 13, 20],
        },
        {
          name: 'Agriculture',
          data: [5, 3, 8, 26],
        },
      ],

         computed:{
      ...mapState('bailleur', {
        secteurs: state => state.secteurs,
        errors: state => state.errors,
      })
  },
    }
  },
}
</script>     
