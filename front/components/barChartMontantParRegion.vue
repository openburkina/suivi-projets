<template>
  <BarChart  :options="montants.options" :series="montants.series" />
</template>
<script>

import {mapState} from 'vuex'

export default {
  computed: {
    ...mapState('region', {
      montants: (state) => state.montants,
      errors: (state) => state.errors
    }),
  },

}
</script>