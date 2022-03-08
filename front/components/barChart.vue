<template>
  <apexchart type="bar" :options="options" :series="series"></apexchart>
</template>
<script>
export default {
  props: ['series', 'options'],
}
</script>
