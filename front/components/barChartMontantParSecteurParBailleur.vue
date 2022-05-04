<template>
  <div>
      <BarChart :options="options" :series="series_secteurs"/>
  </div>
</template>
<script>

import {mapState} from 'vuex'

export default {
  data() {
    return {
     options: {
        chart: {
          id: 'bar-chart-montant-secteur',
        },
        xaxis: {
           categories: ['Sécurité', 'Santé', 'Éducation', 'Agriculture'],
          //categories: this.bailleurs_label,
        },
        colors: '#00E396',
      },
    }
  },
  computed:{
      ...mapState('bailleur', {
        series_secteurs: state => state.series_secteurs,
        bailleurs_label: state => state.bailleurs_label,
        errors: state => state.errors,
      })
  },
}
</script>