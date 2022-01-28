<template>
  <v-card class="mx-auto" max-width="900">
    <Title value="Information sur le projet" />
    <v-list-item>
      <v-list-item-title>ID</v-list-item-title>
      <v-list-item-subtitle>{{ projet.id }}</v-list-item-subtitle>
    </v-list-item>
    <v-divider></v-divider>
    <v-list-item>
      <v-list-item-title>Bailleur</v-list-item-title>
      <v-list-item-subtitle>{{ projet.bailleur }}</v-list-item-subtitle>
    </v-list-item>
    <v-divider></v-divider>
    <v-list-item>
      <v-list-item-title>Exécutant</v-list-item-title>
      <v-list-item-subtitle>{{ projet.executant }}</v-list-item-subtitle>
    </v-list-item>
    <v-divider></v-divider>
    <v-list-item>
      <v-list-item-title>Secteur</v-list-item-title>
      <v-list-item-subtitle>{{ projet.secteur }}</v-list-item-subtitle>
    </v-list-item>
    <v-divider></v-divider>
    <v-list-item>
      <v-list-item-title>Région</v-list-item-title>
      <v-list-item-subtitle>{{ projet.région }}</v-list-item-subtitle>
    </v-list-item>
    <v-divider></v-divider>
    <v-list-item>
      <v-list-item-title>Statut</v-list-item-title>
      <v-list-item-subtitle>{{ projet.statut }}</v-list-item-subtitle>
    </v-list-item>
    <v-divider></v-divider>
    <v-list-item>
      <v-list-item-title>Budget</v-list-item-title>
      <v-list-item-subtitle>{{ projet.budget }}</v-list-item-subtitle>
    </v-list-item>
    <v-divider></v-divider>
    <v-list-item>
      <v-list-item-title>Date de dernière mise à jour</v-list-item-title>
      <v-list-item-subtitle>{{ projet.dateDerniereMAJ }}</v-list-item-subtitle>
    </v-list-item>
  </v-card>
</template>
<script>
export default {
  props: ['projet'],
}
</script>
