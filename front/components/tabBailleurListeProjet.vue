<template>
  <div>
    <Title value="Liste des projets du bailleur"></Title>
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
        { text: 'Bénéficiaires', value: 'beneficiary', width: "130px" },
        { text: 'Titre', value: 'title' },
        { text: 'Secteurs', value: 'sector', width: "130px" },
        { text: 'Régions', value: 'region' , width: "130px"},
        { text: 'Montant', value: 'budgetT' },
        { text: 'Etape', value: 'stage', width: "100px" },
        { text: 'Année de début', value: 'start_date'},
        { text: 'Année de fin', value: 'finish_date', width: "10px"},
      ],
    }
  },
  methods: {
    createEditLink(item) {
      return this.$router.push({ path: '/projets/detail/' + item.project_id })
    },
  },
  computed: {
    ...mapState('bailleur', {
      projects: (state) => state.projects,
      errors: (state) => state.errors,
    }),
  },
}
</script>
<style>
th .text-start {
  color: red;
}
</style>
