<template>
  <div>
    <Title value="Liste des projets de la région"></Title>
    <v-card class="mx-auto px-3">
      <v-data-table
        :headers="headersProjets"
        :items="projects"
        :search="search"
        @click:row="createEditLink"
      >
      </v-data-table>
    </v-card>
  </div>
</template>
<script>
import { mapState } from 'vuex'

export default {
  props: ['search'],
  data() {
    return {
      headersProjets: [
        {
          text: 'ID',
          align: 'start',
          sortable: false,
          value: 'project_id',
        },
        { text: 'Bénéficiaires', value: 'beneficiary' },
        { text: 'Titre', value: 'title' },
        { text: 'Secteurs', value: 'sector' },
        { text: 'Régions', value: 'organisation' },
        { text: 'Montant', value: 'budgetT' },
        { text: 'Etape', value: 'stage' },
        { text: 'Année de début', value: 'start_date' },
        { text: 'Année de fin', value: 'finish_date' },
      ],
    }
  },
  methods: {
    createEditLink(item) {
      return this.$router.push({ path: '/projets/detail/' + item.project_id })
    },
  },
  computed: {
    ...mapState('region', {
      projects: (state) => state.projects,
      errors: (state) => state.errors,
    }),
  },
}
</script>
