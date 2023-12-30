<template>
  <div>
   <Titre title="Liste des bailleurs intervenant dans le pays" />
    <v-card color="indigo lighten-5 elevation-4 mx-4 mt-4 mb-16">
      <v-card-title>
        Liste des bailleurs
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
        :items="buyers"
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
export default {
  data(){
    return {
      search:'',
      headers: [
        {
            align: 'start',
            sortable: false,
         
          },
        { text: 'id', value: 'organizationid.id' },
        { text: 'Nom', value: 'organizationid.narrative' },
        { text: 'type', value: 'organizationid.type' },
       
      ],
    }
  },

  mounted(){
     this.$store.dispatch('fetchOrganisation')
  },
 
  computed:{
    buyers(){
      return this.$store.state.organisationList
    },
    done(){
      return this.$store.state.organisationDetails.length
    },
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
    createEditLink(buyer) {
      this.$store.state.particularName = `Projet de : ${buyer.organizationid.narrative }`
      return this.$router.push({ path: '/bailleurs/' + buyer.organizationid.id})
    },
  },
}
</script>
