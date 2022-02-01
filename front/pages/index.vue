<template>
<no-ssr>
  


  <div>
    <!-- MAP : Montant totaux des projets par régions -->
    <Title value="Carte" />
    <Leaflet />

    <!-- CHART : Statistiques sur les projets -->
    <Title value="Statistiques" />
    <v-row>
      <v-col cols="6">
        <v-card class="mx-auto">
          <v-card-title class="text-h5">Statut des projets</v-card-title>
          <v-card-subtitle
            >Pourcentage des projes t&eacute;rmin&eacute;s et en
            cours</v-card-subtitle
          >
          <v-divider></v-divider>
          <DonutChartStatutProjet/> 
        </v-card>
      </v-col>
      <v-col cols="6">
        <v-card class="mx-auto">
          <v-card-title class="text-h5">Montant par secteurs</v-card-title>
          <v-card-subtitle
            >Evolutions des montants par secteurs</v-card-subtitle
          >
          <v-divider></v-divider>
        <LineChartMontantParSecteur/> 
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
         <BarChartMontantParRegion/> 
          </v-card
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
        <BarChartMontantParSecteur/> 
          </v-card
      ></v-col>
    </v-row>
  </div>
  </no-ssr>
</template>
<script>
export default {
  data() {
    return {
    }
  },
}
</script>
