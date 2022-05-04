<template>
<div>
 
  <BarChart :options="options" :series="series" />
  </div>
</template>
<script>
export default {
  data() {
    return {
     options: {
        chart: {
          id: 'bar-chart-montant-secteur',
        },
        xaxis: {
          categories: ['Sécurité', 'Santé', 'Éducation', 'Agriculture'],
        },
        colors: '#00E396',
      },
      series: [
        {
          name: 'Secteurs',
          data: [30, 40, 35, 50],
        },
      ],

    }
  },
}
</script>
