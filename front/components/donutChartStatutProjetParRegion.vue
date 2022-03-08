<template>
  <v-row class="mx-auto">
    <v-col cols="6" v-for="t in montantStatusParRegion" :key="t"
      ><DonutChart :options="t.options" :series="t.series"
    /></v-col>
  </v-row>
</template>
<script>
import { mapState } from 'vuex'

export default {
  computed: {
    ...mapState('region', {
      montantStatusParRegion: (state) => state.montantStatusParRegion,
      errors: (state) => state.errors,
    }),
  },
}
</script>
