<template>
  <apexchart
    type="line"
    :options="options"
    :series="series"
  ></apexchart>
</template>
<script>
export default {
  props: ['series', 'options'],
}
</script>
