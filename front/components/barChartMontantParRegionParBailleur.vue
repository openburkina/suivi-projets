<template>
  <BarChart :options="options" :series="series_regions" />
</template>
<script>

import {mapState} from 'vuex'

export default {
  data() {
    return {
     options: {
        chart: {
          id: 'bar-chart-montant-region',
        },
        xaxis: {
          categories: ['Iraq', 'Afghanistan', 'Tunisie', 'Afrique du Sud'],
        },
        colors: '#008FFB',
      },
    }
  },

  computed:{
      ...mapState('bailleur', {
        series_regions: state => state.series_regions,
        errors: state => state.errors,
      })
  },
}
</script>
