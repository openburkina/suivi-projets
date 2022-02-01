<template>
  <div>
    <v-select
      :items="regions"
      item-text="name"
      item-value="region_code"
      label="Selectionnez une région"
    ></v-select>
    <v-select
      :items="bailleurs"
      item-text="org_name"
      item-value="ref_id"
      label="Selectionnez un bailleur"
    ></v-select>
  </div>
</template>
<script>
import { mapState } from 'vuex'
export default {
  // async asyncData({ store }) {
  //   await Promise.all([
  //     store.dispatch('region/getRegionsData'),
  //     store.dispatch('bailleur/getBailleursData'),
  //   ])
  //   return
  // },

  // data() {
  //   return {}
  // },

  // computed: {
  //   ...mapState('region', {
  //     regions: (state) => state.regions,
  //     errors: (state) => state.errors,
  //   }),
  //   ...mapState('bailleur', {
  //     bailleurs: (state) => state.bailleurs,
  //     errors: (state) => state.errors,
  //   }),
  // },




  //   async asyncData({ $axios }) {
  //     let { data } = await $axios.get('/menu')
  //     return { regions: data }
  //   },
  //   methods: {
  //     async getIncidents() {
  //       let res = await this.$store.dispatch('getIncidents')
  //       this.regions = res.data
  //     },
  //   },
}
</script>
