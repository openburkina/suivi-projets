<template>
  <div>
    <v-card>
      <v-tabs
        v-model="tab"
        background-color="indigo lighten-5"
        centered
        icons-and-text
      >
        <v-tabs-slider></v-tabs-slider>

        <v-tab href="#tab-1">
          Liste
          <v-icon>mdi-view-list</v-icon>
        </v-tab>

        <v-tab href="#tab-2">
          Statistiques
          <v-icon>mdi-chart-bar</v-icon>
        </v-tab>
        <v-spacer></v-spacer>
        <v-select
        :items="bailleurs"
        v-model="bailleur"
        label="Choose bailleur"
        item-text="title"
        bottom
        autocomplete
        >
      </v-select>
      </v-tabs>

      <v-tabs-items v-model="tab" class="mb-9">
        <v-tab-item value="tab-1" class="mb-9">
          <Title :value="getTitle(`Liste`)"></Title>
          <v-card class="mx-auto px-3">
            <v-data-table
              :headers="headersProjets"
              :items="projets"
              :search="search"
            >
            </v-data-table>
          </v-card>
        </v-tab-item>
        <v-tab-item value="tab-2">
          <Title :value="getTitle(`Stastistique`)"></Title>
          <v-card class="mx-auto px-3"> </v-card>
        </v-tab-item>
      </v-tabs-items>
    </v-card>
  </div>
</template>
<script>
export default {
  data() {
    return {
     bailleur: null,
      bailleurs: [
        { id: "1111", manager: 'Alice',  title: 'Water Cart 1' },
        { id: "2222", manager: 'Bob',    title: 'Water Cart 2' },
        { id: "3333", manager: 'Neysa',  title: 'Water Cart 3' }
      ],
      search: '',
      headersProjets: [
        {
          text: 'ID',
          align: 'start',
          sortable: false,
          value: 'id',
        },
        { text: 'Bénéficiaires', value: 'beneficiaire' },
        { text: 'Titre', value: 'titre' },
        { text: 'Secteurs', value: 'secteurs' },
        { text: 'Régions', value: 'regions' },
        { text: 'Montant', value: 'montant' },
        { text: 'Etape', value: 'etape' },
        { text: 'Année de début', value: 'anneeDebut' },
        { text: 'Année de fin', value: 'anneeFin' },
        { text: 'Dernière mise a jour', value: 'derniereMAJ' },
      ],
      projets: [
        {
          id: 11110,
          beneficiaire: 'NHU JIJ 12',
          titre: 'PRJ 8923',
          secteurs: 'Agriculture',
          regions: 'Iraq',
          montant: 98454.434,
          etape: 'Initialisation',
          anneeDebut: '2022-01-03',
          anneeFin: '2022-01-12',
          derniereMAJ: '2022-01-12',
        },
        {
          id: 7887,
          beneficiaire: 'LMN NJN 12',
          titre: 'PRJ 892',
          secteurs: 'Santé',
          regions: 'Afghanistan',
          montant: 834.434,
          etape: 'Initialisation',
          anneeDebut: '2022-01-03',
          anneeFin: '2022-01-12',
          derniereMAJ: '2022-01-12',
        },
      ],
      idBailleurs: 187,
      tab: null,
    }
  },
  methods: {
    getTitle(message) {
      return `${message}  des projets sur le bailleur : ${this.idBailleurs}`
    },
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
