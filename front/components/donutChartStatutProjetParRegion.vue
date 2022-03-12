<template>
  <DonutChart :options="options" :series="series" />
</template>
<script>
export default {
  data() {
    return {
      options: {
        labels: ['Términé', 'En cours'],
      },
      series: [50, 66],
    }
  },
  
}
</script>
