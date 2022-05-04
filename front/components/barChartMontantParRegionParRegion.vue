<template>
  <BarChart :options="options" :series="series" />
</template>
<script>
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
      series: [
        {
          name: 'Pays',
          data: [30, 40, 35, 50],
        },
      ],
    }
  },
}
</script>
