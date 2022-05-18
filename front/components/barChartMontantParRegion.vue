<template>
  <div>
    <BarChart :options="montants.options" :series="montants.series" />
  </div>
</template>
<script>
import { mapState, mapActions } from 'vuex'

export default {
  computed: {
    ...mapState('region', {
      regions: (state) => state.regions,
      montants: (state) => state.montants,
      // test: (state) => {
      //   let opt = JSON.parse(JSON.stringify(state.montants));
      //   const regs = state.regions;
      //   opt['series'].map(serie => {
      //     const val = regs.find(re => re.region_code == serie.name)
      //     serie.name = val.name;
      //   })
      //   return opt;
      // },
      errors: (state) => state.errors,
    }),
  },
  methods: {
    btnClick(){
      let dataa = JSON.stringify(this.$store.state.errors);
      console.log(dataa)
      // dataa[0] = 'huhu';
      // this.$store.commit('region/SET_ERRORS', dataa);
    }
  }
}
</script>
