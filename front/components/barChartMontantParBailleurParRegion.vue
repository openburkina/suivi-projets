<template>
    <BarChart :options="montantBailleur.options" :series="montantBailleur.series" />
</template>
<script>
import { mapState } from 'vuex'

export default {
  computed: {
    ...mapState('region', {
      regions: (state) => state.regions,
      montantBailleurParRegion: (state) => state.montantBailleurParRegion,
      bailleurs: (state) => state.bailleurs,
      montantBailleur: (state) => {
        let opt = JSON.parse(JSON.stringify(state.montantBailleurParRegion));
        const baills = state.bailleurs;
        opt['series'].map(serie => {
          const val = baills.find(bai => bai.ref_id == serie.name)
          serie.name = val.org_name;
        })
        return opt;
      },
      errors: (state) => state.errors,
    }),
  },
}
</script>
