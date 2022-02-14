<template>
  <v-data-table
    :headers="headers"
    :items="projets"
    :search="search"
    class="elevation-1"
    @click:row="createEditLink"
  >
    <template v-slot:[`item.activity_status`]="{ item }">
      <v-chip :color="getColor(item.activity_status)" dark>
        <v-icon size="24px">
          {{ getValue(item.activity_status) }}
        </v-icon>
      </v-chip>
    </template>
  </v-data-table>
</template>
<script>
import {mapState} from 'vuex'
import { global } from '~/mixins/global.js'

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
        { text: 'Bailleur', value: 'org_name' },
        { text: 'Exécutant', value: 'operating_unit' },
        { text: 'Secteur', value: 'sector' },
        { text: 'Région', value: 'region' },
        { text: 'Statut', value: 'activity_status' },
        { text: 'Budget', value: 'budgetT' },
        // { text: 'Date de dernière mise à jour', value: 'dateDerniereMAJ' },
      ],
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
      return this.$router.push({ path: '/projets/detail/' + item.project_id })
    },
  },
  computed: {
    ...mapState('project', {
      projets: (state) => state.projects,
      errors: (state) => state.errors,
    }),
  },
}
</script>
