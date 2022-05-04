<template>
  <div>
    <Title value="Liste des projets"></Title>
    <v-card color="indigo lighten-5">
      <v-card-title>
        Projets
        <v-spacer></v-spacer>
        <v-text-field
          v-model="search"
          append-icon="mdi-magnify"
          label="Recherche"
          single-line
          hide-details
        ></v-text-field>
      </v-card-title>
      <DatatableProjets :search="search"/>
    </v-card>
  </div>
</template>
<script>

import {mapState} from 'vuex'

export default {
  data() {
    return {
      search: ''
    }
  },

   async asyncData({store}){
      await Promise.all([
        store.dispatch('project/getProjectsData')
      ])
      return
    },

  

}
</script>