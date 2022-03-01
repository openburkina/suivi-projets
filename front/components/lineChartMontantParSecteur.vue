<template>
  <LineChart :options="montants.options" :series="montants.series" />
</template>
<script>

import {mapState} from 'vuex'

export default {
  computed: {
    ...mapState('secteur', {
      montants: (state) => state.montants,
      errors: (state) => state.errors
    }),
  },

}
</script>
