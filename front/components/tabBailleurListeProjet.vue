<template>
  <div>
    <Title value="Liste des projets du bailleur"></Title>
    <v-card class="mx-auto px-3">
      <v-data-table :headers="headersProjets" :items="bailleurs" :search="search">
      </v-data-table>
    </v-card>
  </div>
</template>
<script>
import {  mapState } from 'vuex'

export default {
  props:['search'],

  async asyncData({ store }) {
    await Promise.all([
      store.dispatch('bailleur/getBailleursData'),
    ])
    return
  },

  computed: {
    ...mapState('bailleur', {
      bailleurs: (state) => state.bailleurs,
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
          value: 'ref_id',
        },
        { text: 'Bailleur', value: 'org_name' },
      ],
    }
  },
}
</script>
