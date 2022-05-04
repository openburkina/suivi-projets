<template>
<div> 

  <v-data-table
    :headers="headers"
    :items="regions"
    :search="search"
    class="elevation-1"
    @click:row="createEditLink"
  >
  </v-data-table>

</div>
</template>
<script>

import {mapState, mapActions} from 'vuex'

export default {
  props: ['search'],
  data() {
    return {
      headers: [
        { text: 'Nom de la région', value: 'name' },
        { text: 'Code de la région', value: 'region_code' },
      ],

       // lats: [],

    }
  },

  methods: {
    createEditLink(item) {
      return this.$router.push({ path: '/regions/projets/' + item.region_code })
    },
  },

  computed: {
    ...mapState('region', {
      regions: (state) => state.regions,
      errors: (state) => state.errors,
    }),
  },

}
</script>