<template>
<div>
  <v-data-table
    :headers="headers"
    :items="projets"
    :search="search"
    class="elevation-1"
    @click:row="createEditLink"
  >

    <template v-slot:[`item.statut`]="{ item }">
      <v-chip :color="getColor(item.activity_status)" dark>
        <v-icon size="24px">
          {{ getValue(item.activity_status) }}
        </v-icon>
      </v-chip>
    </template>
  </v-data-table>
  </div>
</template>
<script>

import {mapState} from 'vuex'

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
        { text: 'Intitulé', value: 'title' },
        { text: 'Region', value: 'region', width:'150px'  },
        { text: 'Bailleur', value: 'org_name'},
        { text: 'Statut', value: 'statut', width:'120px' },
        { text: 'Budget', value: 'budgetT', width:'150px' },
      ],
    


 async asyncData({store}){
      await Promise.all([
        store.dispatch('project/getProjectsData'),
      ])
      return
    },

    }

  },
  methods: {
    getColor(statut) {
      if (statut < 1) return '#00E396'
      else return '#008FFB'
    },
    getValue(statut) {
      if (statut < 1) return 'mdi-close'
      else return 'mdi-check'
    },
    createEditLink(item) {
      return this.$router.push({ path: '/projets/details/' + item.project_id })
    },
  },

   computed:{
      ...mapState('project', {
        projets: state => state.projects,
        errors: state => state.errors,
      })
    },
}
</script>