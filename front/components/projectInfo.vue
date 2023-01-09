<template>
<div>
    <Titre title="A propos du projets" />
  <v-card class="mx-auto" max-width="900">
    <v-list-item>
      <v-list-item-title>Titre</v-list-item-title>
      <v-list-item-subtitle>{{ info[0].titre }}</v-list-item-subtitle>
    </v-list-item>
    <v-divider></v-divider>
    <v-list-item>
      <v-list-item-title>Bailleur</v-list-item-title>
      <v-list-item-subtitle>{{ info[0].bailleur }}</v-list-item-subtitle>
    </v-list-item>
    <v-divider></v-divider>
    <v-list-item>
      <v-list-item-title>Executant</v-list-item-title>
      <v-list-item-subtitle>{{ info[0].executant }}</v-list-item-subtitle>
    </v-list-item>
    <v-divider></v-divider>
    <v-list-item>
      <v-list-item-title>Budget</v-list-item-title>
      <v-list-item-subtitle>{{ info.budget }}</v-list-item-subtitle>
    </v-list-item>
    <v-divider></v-divider>
    <v-list-item>
      <v-list-item-title>Région</v-list-item-title>
      <v-list-item-subtitle>{{ info[0].region }}</v-list-item-subtitle>
    </v-list-item>
    <v-divider></v-divider>
    <v-list-item>
      <v-list-item-title>Secteur</v-list-item-title>
      <v-list-item-subtitle>{{ info[0].secteur }}</v-list-item-subtitle>
    </v-list-item>
    <v-divider></v-divider>
    <v-list-item>
      <v-list-item-title>Conditions</v-list-item-title>
      <v-list-item-subtitle>{{ info[0].conditions }}</v-list-item-subtitle>
    </v-list-item>
    <v-divider></v-divider>
    <v-list-item>
      <v-list-item-title>Statut</v-list-item-title>
      <v-list-item-subtitle>{{ info[0].statut }}</v-list-item-subtitle>
    </v-list-item>
    <v-divider></v-divider>
    <v-list-item>
      <v-list-item-title>Date debut</v-list-item-title>
      <v-list-item-subtitle>{{ info[0].datedebut }}</v-list-item-subtitle>
    </v-list-item>
    <v-divider></v-divider>
    <v-list-item>
      <v-list-item-title>Date fin</v-list-item-title>
      <v-list-item-subtitle>{{ info[0].datefin }}</v-list-item-subtitle>
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