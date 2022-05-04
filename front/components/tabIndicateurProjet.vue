<template>
  <div>
    <Title value="Indicateurs du projet"></Title>
    <v-card class="mx-auto px-3">
      <v-data-table
        :headers="headersIndicateurs"
        :items="indicators"
        :search="search"
        class="elevation-0"
      >
        <!-- <template v-slot:[`item.statutCible`]="{ item }">
                <v-chip :color="getColor(item.statutCible)" dark>
                  <v-icon size="24px">
                    {{ getValue(item.statutCible) }}
                  </v-icon>
                </v-chip>
              </template> -->
      </v-data-table>
    </v-card>
  </div>
</template>
<script>

import {  mapState } from 'vuex'

export default {
  props: ['search'],
  data() {
    return {
      headersIndicateurs: [
        {
          text: 'ID',
          align: 'start',
          sortable: false,
          value: 'project_id',
        },
        { text: 'Titre', value: 'titre' },
        { text: 'Référence', value: 'reference' },
        { text: 'Période référence', value: 'reference_period'},
        { text: 'Cible', value: 'target'},
        { text: 'Période Cible', value: 'target_period'},
        { text: 'Statut Cible', value: 'target_status'},
      ]
    }
  },

  computed:{
      ...mapState('project', {
        indicators: state=> state.indicators,
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
