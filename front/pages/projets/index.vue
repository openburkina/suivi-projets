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
export default {
  data() {
    return {
      search: '',
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
      return this.$router.push({ path: '/projets/detail/' + item.id })
    },
  },
}
</script>
