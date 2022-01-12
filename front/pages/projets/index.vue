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
      <v-data-table
        :headers="headers"
        :items="projets"
        :search="search"
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
  data() {
    return {
      search: '',
      headers: [
        {
          text: 'ID',
          align: 'start',
          sortable: false,
          value: 'id',
        },
        { text: 'Bailleur', value: 'bailleur' },
        { text: 'Exécutant', value: 'executant' },
        { text: 'Secteur', value: 'secteur' },
        { text: 'Région', value: 'région' },
        { text: 'Statut', value: 'statut' },
        { text: 'Budget', value: 'budget' },
        { text: 'Date de dernière mise à jour', value: 'dateDerniereMAJ' },
      ],
      projets: [
        {
          id: 78366,
          bailleur: 'UNSFC',
          executant: 'EXC 780',
          secteur: 'Santé',
          région: 'Iraq',
          statut: 1,
          budget: 12849585.94,
          dateDerniereMAJ: '2021-12-12',
        },
        {
          id: 88466,
          bailleur: 'JIJN',
          executant: 'LONM 754',
          secteur: 'Agricutlure',
          région: 'Afghanistan',
          statut: -1,
          budget: 8779344.94,
          dateDerniereMAJ: '2021-11-23',
        },
        {
          id: 90475,
          bailleur: 'NJDD',
          executant: 'OLNM 098',
          secteur: 'Sécurité',
          région: 'Iraq',
          statut: -1,
          budget: 78578.94,
          dateDerniereMAJ: '2021-09-12',
        },
      ],
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
