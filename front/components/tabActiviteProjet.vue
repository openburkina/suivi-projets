<template>
  <v-card class="mx-auto px-3">
    <Title value="Activités sur le projet" />
    <v-data-table
      :headers="headers"
      :items="activities"
      :search="search"
      class="elevation-0"
    >
      <!-- <template v-slot:[`item.statut`]="{ item }">
        <v-chip :color="this.getColor1(item.statut)" dark>
          <v-icon size="24px">
            {{ this.getValue1(item.statut) }}
          </v-icon> 
        </v-chip>
      </template> -->
    </v-data-table>
     <!-- <h2>{{this.getColor1(1)}},{{this.getValue1(1)}}</h2>  -->
  </v-card>
</template>
<script>

import {  mapState } from 'vuex'

export default {
  props: ['search'],
  data() {
    return {
      headers: [
        {
          text: 'ID',
          align: 'start',
          sortable: false,
          value: 'project_id',
        },
        { text: 'Titre', value: 'title' },
        { text: 'Date début', value: 'start_date' },
        { text: 'Date fin', value: 'finish_date' },
        { text: 'Montant', value: 'amount_act' },
        { text: "Acteurs d'éxecutions", value: 'Actors_partner' },
        { text: 'Acteurs partenaires', value: 'Actors_execution' },
        { text: 'Année de planifications', value: 'year_plan' },
      ],
    }
  },

    computed:{
      ...mapState('project', {
        activities: state=> state.activities,
        errors: state=> state.errors
      })
    },

    methods: {
      getColor(statut) {
        if (statut < 1) return '#00E396'
        else return '#008FFB'
      },
      getValue(statut) {
        if (statut < 1) return 'mdi-close'
        else return 'mdi-check'
      }
  },


}
</script>
