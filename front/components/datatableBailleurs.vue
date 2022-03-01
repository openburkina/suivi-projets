<template>
  <v-data-table
    :headers="headers"
    :items="baillleurs"
    :search="search"
    class="elevation-1"
    @click:row="createEditLink"
  >
  </v-data-table>
</template>
<script>

import {mapState} from 'vuex'

export default {
  props: ['search'],
  data() {
    return {
      headers: [
        { text: 'Code du bailleur', value: 'ref_id' },
        { text: 'Nom du bailleur', value: 'org_name' },
      ],
    }
  },
  methods: {
    createEditLink(item) {
      return this.$router.push({ path: '/bailleurs/projets/' + item.ref_id })
    },
  },
  computed: {
    ...mapState('bailleur', {
      baillleurs: (state) => state.baillleurs,
      errors: (state) => state.errors,
    }),
  },
}
</script>
