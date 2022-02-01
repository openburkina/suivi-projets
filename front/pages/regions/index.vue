<template>
  <div>
    <TabRegionContent/>
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
}
</script>