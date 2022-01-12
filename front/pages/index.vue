<template>
  <div>
    <!-- CAROUSEL -->
    <v-carousel cycle hide-delimiters show-arrows-on-hover height="500">
      <v-carousel-item
        v-for="(item, i) in items"
        :key="i"
        :src="item.src"
      ></v-carousel-item>
    </v-carousel>

    <!-- MAP : Montant totaux des projets par régions -->
    <Title value="Maps"></Title>
    <Leaflet />

    <!-- CHART -->
    <Title value="Statistiques"></Title>
    <v-row>
      <v-col cols="6">
        <v-card class="mx-auto">
          <v-card-title class="text-h5">Statut des projets</v-card-title>
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
          <v-card-title class="text-h5">Montant par secteurs</v-card-title>
          <v-card-subtitle
            >Evolutions des montants pour les secteurs de la sécurité, santé,
            éducation et agriculture</v-card-subtitle
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
      // CAROUSEL DATA
      //
      items: [
        {
          src: require('~/assets/img/image3.jpg'),
        },
        {
          src: require('~/assets/img/image1.jpg'),
        },
        {
          src: require('~/assets/img/image2.jpg'),
        },
      ],
    }
  },
}
</script>
