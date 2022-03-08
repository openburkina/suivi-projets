<template>
<div>
  <apexchart type="bar" :options="options" :series="series"></apexchart>
  <p>{{config()}}</p>
</div>
</template>
<script>
export default {
  props: ['series', 'options', 'regions'],
  data: {
    test: [],
  },
  methods: {
    config() {
      let test = this.series;
      let test1 = this.regions;
      test.forEach(serie => {
        const region = test1.forEach(reg => {
          if (serie.name == reg.region_code){
            return serie;
          }
        })
        console.log(region)
        // serie.name = region.name
      });
      return test
      // return this.series.map(serie => {
      //   const region = this.regions.find(region => region.region_code === serie.name).name;
      //   serie.name = region;
      // });
    },
  },
}
</script>
