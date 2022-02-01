<template>
  <div>
    <Title value="Liste des projets de la région"></Title>
    <v-card class="mx-auto px-3">
      <v-data-table :headers="headersProjets" :items="regions" :search="search">
      </v-data-table>
    </v-card>
  </div>
</template>
<script>

import {  mapState } from 'vuex'

export default {
  props:['search'],
  computed: {
    ...mapState('region', {
      regions: (state) => state.regions,
      errors: (state) => state.errors,
    }),
  },


  data() {
    return {
      headersProjets: [
        {
          text: 'ID',
          align: 'start',
          sortable: false,
          value: 'id',
        },
        { text: 'Region', value: 'name' },
        { text: 'Code de la region', value: 'region_code' },
      ],
    }
  },
}
</script>
