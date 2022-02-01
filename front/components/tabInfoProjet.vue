<template>
  <v-card class="mx-auto" max-width="900">
    <Title value="Information sur le projet" />
<!-- 
    <v-list-item>
      <v-list-item-title>ID</v-list-item-title>
      <v-list-item-subtitle>{{ projet.id }}</v-list-item-subtitle>
    </v-list-item>
    <v-divider></v-divider>
    <v-list-item>
      <v-list-item-title>Bailleur</v-list-item-title>
      <v-list-item-subtitle>{{ projet.bailleur }}</v-list-item-subtitle>
    </v-list-item>
    <v-divider></v-divider>
    <v-list-item>
      <v-list-item-title>Exécutant</v-list-item-title>
      <v-list-item-subtitle>{{ projet.executant }}</v-list-item-subtitle>
    </v-list-item>
    <v-divider></v-divider>
    <v-list-item>
      <v-list-item-title>Secteur</v-list-item-title>
      <v-list-item-subtitle>{{ projet.secteur }}</v-list-item-subtitle>
    </v-list-item>
    <v-divider></v-divider>
    <v-list-item>
      <v-list-item-title>Région</v-list-item-title>
      <v-list-item-subtitle>{{ projet.région }}</v-list-item-subtitle>
    </v-list-item>
    <v-divider></v-divider>
    <v-list-item>
      <v-list-item-title>Statut</v-list-item-title>
      <v-list-item-subtitle>{{ projet.statut }}</v-list-item-subtitle>
    </v-list-item>
    <v-divider></v-divider>
    <v-list-item>
      <v-list-item-title>Budget</v-list-item-title>
      <v-list-item-subtitle>{{ projet.budget }}</v-list-item-subtitle>
    </v-list-item>
    <v-divider></v-divider>
    <v-list-item>
      <v-list-item-title>Date de dernière mise à jour</v-list-item-title>
      <v-list-item-subtitle>{{ projet.dateDerniereMAJ }}</v-list-item-subtitle>
    </v-list-item>
    The List: {{projets}}
     -->
  </v-card>
</template>


<script>

import {  mapState } from 'vuex'
export default {
 props: ['id'],
 async asyncData({store}){
      await Promise.all([
        store.dispatch('project/getProjectsData')
      ])
      return
    },

     data() {
    return {
     idProjet: this.$route.params.project_id,
    }
  },

 computed:{
      ...mapState('project', {
        projets: state => state.projects,
        errors: state => state.errors,
      })
    },

 methods: {
    getTitle(message) {
      return `${message} sur le projet : ${this.idProjet}`
    },
    getProjet() {
      return this.projets.find((p) => p.project_id == this.idProjet)
    },
    getColor(statut) {
      if (statut < 1) return '#00E396'
      else return '#008FFB'
    },
    getValue(statut) {
      if (statut < 1) return 'mdi-close'
      else return 'mdi-check'
    },
  },

}
</script>
