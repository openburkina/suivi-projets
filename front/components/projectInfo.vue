<template>
<div v-if="info.title!=null">
    <Titre title="A propos du projets" />
  <v-card class="mx-auto" max-width="900">
    <v-list-item>
      <v-list-item-title>Titre</v-list-item-title>
      <v-list-item-subtitle>{{ info.title }}</v-list-item-subtitle>
    </v-list-item>
    <v-divider></v-divider>
    <v-list-item>
      <v-list-item-title>Bailleur</v-list-item-title>
      <v-list-item-subtitle>{{ info.organizationid.narrative }}</v-list-item-subtitle>
    </v-list-item>
    <v-divider></v-divider>
    <v-list-item>
      <v-list-item-title>Région</v-list-item-title>
      <v-list-item-subtitle>{{ info.locationid.name }}</v-list-item-subtitle>
    </v-list-item>
    <v-divider></v-divider>
    <v-list-item>
      <v-list-item-title>Secteur</v-list-item-title>
      <v-list-item-subtitle>{{ info.sectorid.narrative }}</v-list-item-subtitle>
    </v-list-item>
    <v-divider></v-divider>
    <v-list-item>
      <v-list-item-title>Statut</v-list-item-title>
      <v-list-item-subtitle>{{ info.activity_status }}</v-list-item-subtitle>
    </v-list-item>
    <v-divider></v-divider>
    <v-list-item>
      <v-list-item-title>Date debut</v-list-item-title>
      <v-list-item-subtitle>{{ info.planned_start }}</v-list-item-subtitle>
    </v-list-item>
    <v-divider></v-divider>
    <v-list-item>
      <v-list-item-title>Date fin</v-list-item-title>
      <v-list-item-subtitle>{{ info.planned_end }}</v-list-item-subtitle>
    </v-list-item>
    <v-divider></v-divider>
    <v-list-item>
      <v-list-item-title>Dernière Mise à jour</v-list-item-title>
      <v-list-item-subtitle>{{ info.last_updated_datetime }}</v-list-item-subtitle>
    </v-list-item>
    <v-divider></v-divider>
  </v-card>
</div>

</template>
<script>
export default {
  props: ['info'],
  methods: {
    getColor(statut) {
      if (statut < 1) return '#00E396'
      else return '#008FFB'
    },
    getValue(statut) {
      if (statut < 1) return 'mdi-close'
      else return 'mdi-check'
    },
  },
}
</script>