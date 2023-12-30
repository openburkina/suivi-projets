<template>
  <div>
   <Titre title="Liste des projets financés par la Banque Mondiale et la BAD" />
    <v-card color="indigo lighten-5 elevation-0 mx-4 mt-4 mb-16">
      <v-card-title>
        Liste des Projets
        <v-spacer></v-spacer>
        <v-text-field
          v-model="search"
          append-icon="mdi-magnify"
          label="Recherche"
          hide-details
          solo
          rounded
        ></v-text-field>
      </v-card-title>
      <v-data-table
        :headers="headers"
        :items="projects"
        :search="search"
        :items-per-page=5
        :options=
        "{sortBy: []}"
        class="elevation-1"
        @click:row="createEditLink"
      >
        <template v-slot:[`item.statut`]="{ item }">
          <v-chip :color="getColor(item.statut)" dark>
            <v-icon size="24px">
              {{ getValue(item.statut) }}
            </v-icon>
          </v-chip>
        </template>
      </v-data-table>
    </v-card>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  data(){
    return {
      search:'',
      headers: [
        {
            align: 'start',
            sortable: false,
         
          },
        { text: 'ID', value: 'identifiant' },
        { text: 'Nom', value: 'titre' },
        { text: 'Bailleur', value: 'bailleur' },
        { text: 'Secteur', value: 'secteur' },
        { text: 'Budget', value: 'montant' },
        { text: 'Date de Debut', value: 'datedebut' },
        { text: 'Date de Fin', value: 'datefin' },
        { text: 'Structure Executante', value: 'executant' },
      ],
    }
  },
  mounted(){
    this.fetchProjects();
  },
 
  computed:{
    projects(){
      return this.$store.state.projectList
    },
  },

  methods: {
    ...mapActions({
      fetchProjects: "fetchProjects"
    }),
    getColor(statut) {
      if (statut < 1) return '#00E396'
      else return '#008FFB'
    },
    getValue(statut) {
      if (statut < 1) return 'mdi-close'
      else return 'mdi-check'
    },
    createEditLink(projet) {
      return this.$router.push({ path: '/projets/' + projet.identifiant})
    }
}
}
</script>
