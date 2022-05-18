<template>
  <div>
    <v-row>
      <v-col cols="3"></v-col>
      <v-col cols="6">
        <v-text-field
          v-model="year"
          label="Année"
          type="number"
          v-on:change="$emit('year-change', $event)"
      /></v-col>
      <v-col cols="3"></v-col>
    </v-row>
    <v-row class="mx-auto">
      <DonutChart
        :options="montantsStatus.options"
        :series="montantsStatus.series"
      />
    </v-row>
  </div>
</template>
<script>
import { mapState } from 'vuex'

export default {
  data() {
    return {
      year: new Date().getFullYear(),
    }
  },

  computed: {
    ...mapState('region', {
      montantsStatus: (state) => state.montantsStatus,
      errors: (state) => state.errors,
    }),
  },
  // watch: {
  //   title(val) {
  //     this.$store.commit('editor/SET_TITLE', {
  //       index: this.block.index,
  //       title: val,
  //     })
  //   },
  // },
}
</script>
