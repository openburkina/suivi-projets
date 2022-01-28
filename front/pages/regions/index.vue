<template>
  <div>
    <TabRegionContent :regions="regions" />
  </div>
</template>

<script>
import {  mapState } from 'vuex'
export default {
  async asyncData({ store }) {
    await Promise.all([
      store.dispatch('region/getRegionsData'),
    ])
    return
  },

  computed: {
    ...mapState('region', {
      regions: (state) => state.regions,
      errors: (state) => state.errors,
    }),
  },
}
</script>