<template>
  <apexchart
    type="donut"
    :options="options"
    :series="series"
  ></apexchart>
</template>
<script>
export default {
  props: ["series","options"]
}
</script>
