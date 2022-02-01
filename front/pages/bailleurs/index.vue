<template>
  <div>
    <TabBailleurContent/>
  </div>
</template>
<script>
import {  mapState } from 'vuex'
export default {

  async asyncData({ store }) {
    await Promise.all([
      store.dispatch('bailleur/getBailleursData'),
    ])
    return
  },

}
</script>