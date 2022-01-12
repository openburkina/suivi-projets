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
          :items="regions"
          v-model="region"
          label="Selectionnez une région"
          item-text="nom"
          item-value="nom"
          bottom
          autocomplete
          v-on:change="changeRegion"
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
          <v-card class="mx-auto px-3">
            <v-row>
              <v-col cols="6">
                <v-card class="mx-auto">
                  <v-card-title class="text-h5"
                    >Statut des projets</v-card-title
                  >
                  <v-card-subtitle
                    >Pourcentage des projes t&eacute;rmin&eacute;s et en
                    cours</v-card-subtitle
                  >
                  <v-divider></v-divider>
                  <apexchart
                    type="donut"
                    :options="chartOptionsD"
                    :series="seriesD"
                    :width="widthChart"
                  ></apexchart>
                </v-card>
              </v-col>
              <v-col cols="6">
                <v-card class="mx-auto">
                  <v-card-title class="text-h5"
                    >Montant par secteurs</v-card-title
                  >
                  <v-card-subtitle
                    >Evolutions des montants pour les secteurs de la sécurité,
                    santé, éducation et agriculture</v-card-subtitle
                  >
                  <v-divider></v-divider>
                  <apexchart
                    type="line"
                    :options="chartOptionsLine"
                    :series="seriesLine"
                    :width="widthChart + 50"
                  ></apexchart>
                </v-card>
              </v-col>
            </v-row>
            <v-row>
              <v-col cols="6"
                ><v-card class="mx-auto">
                  <v-card-title class="text-h5"
                    >Montant par r&eacute;gions</v-card-title
                  >
                  <v-card-subtitle
                    >Montant des projets par r&eacute;gions</v-card-subtitle
                  >
                  <v-divider></v-divider>
                  <apexchart
                    type="bar"
                    :options="chartOptionsBar1"
                    :series="seriesBar1"
                    :width="widthChart"
                  ></apexchart> </v-card
              ></v-col>
              <v-col cols="6"
                ><v-card class="mx-auto">
                  <v-card-title class="text-h5"
                    >Montant par secteurs</v-card-title
                  >
                  <v-card-subtitle
                    >Montant des projets par secteurs</v-card-subtitle
                  >
                  <v-divider></v-divider>
                  <apexchart
                    type="bar"
                    :options="chartOptionsBar2"
                    :series="seriesBar2"
                    :width="widthChart"
                  ></apexchart> </v-card
              ></v-col>
            </v-row>
          </v-card>
        </v-tab-item>
      </v-tabs-items>
    </v-card>
  </div>
</template>
<script>
export default {
  data() {
    return {
        widthChart: 500,
      //
      // BAR1 DATA
      //
      chartOptionsBar2: {
        chart: {
          id: 'vuechart-example',
        },
        xaxis: {
          categories: ['Sécurité', 'Santé', 'Éducation', 'Agriculture'],
        },
        colors: '#00E396',
      },
      seriesBar2: [
        {
          name: 'Secteurs',
          data: [30, 40, 35, 50],
        },
      ],
      //
      // BAR1 DATA
      //
      chartOptionsBar1: {
        chart: {
          id: 'vuechart-example',
        },
        xaxis: {
          categories: ['Iraq', 'Afghanistan', 'Tunisie', 'Afrique du Sud'],
        },
        colors: '#008FFB',
      },
      seriesBar1: [
        {
          name: 'Pays',
          data: [30, 40, 35, 50],
        },
      ],
      //
      // LINE DATA
      //
      chartOptionsLine: {
        chart: {
          id: 'vuechart-example',
        },
        xaxis: {
          categories: ['Sécurité', 'Santé', 'Éducation', 'Agriculture'],
        },
      },
      seriesLine: [
        {
          name: 'Sécurité',
          data: [10, 20, 30, 40],
        },
        {
          name: 'Santé',
          data: [15, 25, 35, 50],
        },
        {
          name: 'Éducation',
          data: [9, 7, 13, 20],
        },
        {
          name: 'Agriculture',
          data: [5, 3, 8, 26],
        },
      ],
      //
      // DONUT DATA
      //
      chartOptionsD: {
        labels: ['Términé', 'En cours'],
      },
      seriesD: [34, 66],
      //
      //
      //
      region: null,
      regions: [
        { id: '283', nom: 'Iraq' },
        { id: '546', nom: 'Afghanistan' },
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
      idRegion: '-',
      tab: null,
    }
  },
  methods: {
    getTitle(message) {
      return `${message}  des projets sur la région : ${this.idRegion}`
    },
    getColor(statut) {
      if (statut < 1) return '#00E396'
      else return '#008FFB'
    },
    getValue(statut) {
      if (statut < 1) return 'mdi-close'
      else return 'mdi-check'
    },
    changeRegion(a) {
      this.idRegion = a
    },
  },
}
</script>
