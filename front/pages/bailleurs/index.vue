<template>
  <div>
    <Title value="Liste des bailleurs"></Title>
    <v-card color="indigo lighten-5">
      <v-card-title>
        Bailleurs
        <v-spacer></v-spacer>
        <v-text-field
          v-model="search"
          append-icon="mdi-magnify"
          label="Recherche"
          single-line
          hide-details
        ></v-text-field>
      </v-card-title>
      <DatatableBailleurs :search="search" />
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
  async asyncData({ store }) {
    await Promise.all([store.dispatch('bailleur/getBailleursData')])
    return
  },
}
</script>
