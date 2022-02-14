<template>
  <client-only>
    <TabBailleurContent :bailleurs="bailleurs" />
  </client-only>
</template>
<script>
import { mapState } from 'vuex'
export default {
  async asyncData({ store }) {
    await Promise.all([store.dispatch('bailleur/getBailleursData')])
    return
  },

  computed: {
    ...mapState('bailleur', {
      bailleurs: (state) => state.bailleurs,
      errors: (state) => state.errors,
    }),
  },
}
</script>
