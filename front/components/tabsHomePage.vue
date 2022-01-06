<template>
<v-container fluid>  
    <!-- MAP : Montant totaux des projets par régions -->
    <Leaflet />

    <!-- CHART -->
    <Title value="Statistiques"/>
    <v-select
          :items="getAnnee()"
          label="Années"
          class="ml-5 mr-5"
        ></v-select>
    <v-row no-gutters class="my-5">
      <!-- STATUT DES PROJETS -->
      <v-col md="5" class="ml-12">
        <v-card
          outlined
          tile
          elevation="5"
        >
        <v-card-title>Status des projets</v-card-title>
        <v-divider></v-divider>
         <PieChart :chartData="chartDataStatutProjet" class="py-5"/>
        </v-card>
      </v-col>
      <v-col md="1">
      </v-col>
      <v-col md="5">
        <v-card
          outlined
          tile
          elevation="5"
        >
        <v-card-title>Evolution des montants par secteurs</v-card-title>
        <v-divider></v-divider>
         <LineChart :chartData="chartDataEvolutionMontant" class="py-5"/>
        </v-card>
      </v-col>
    </v-row>
    <v-row no-gutters class="my-5">
      <!-- STATUT DES PROJETS -->
      <v-col md="5" class="ml-12">
        <v-card
          outlined
          tile
          elevation="5"
        >
        <v-card-title>Montants par région</v-card-title>
        <v-divider></v-divider>
         <BarChart :chartData="chartDataMontantParRegion" class="py-5"/>
        </v-card>
      </v-col>
      <v-col md="1">
      </v-col>
      <v-col md="5">
        <v-card
          outlined
          tile
          elevation="5"
        >
        <v-card-title>Montants par secteurs</v-card-title>
        <v-divider></v-divider>
         <BarChart :chartData="chartDataMontantParSecteur" class="py-5"/>
        </v-card>
      </v-col>
    </v-row>
</v-container>
</template>
<script>
  export default {
    data(){
      return {
            chartDataMontantParRegion:{
              labels: ["Iraq","Afghanistan","Argentina","Dominican Republic"],
                datasets: [{
                    label: 'My BarChart',
                    data: [65, 59, 80, 81],
                    backgroundColor: ['#d2d6de', '#a2d6de', '#b2d6de', '#c2d6de'],
                    borderColor: 'rgb(75, 192, 192)',
                    tension: 0.1
                }]
            },
            chartDataMontantParSecteur:{
              labels: ['Sécurité', 'Santé', 'Education', 'Agriculture'],
               datasets: [{
                    label: 'My BarChart',
                    data: [65, 59, 80, 81],
                    backgroundColor: ['#d2d6de', '#a2d6de', '#b2d6de', '#c2d6de'],
                    borderColor: 'rgb(75, 192, 192)',
                    tension: 0.1
                }]
            },
            chartDataStatutProjet:{
              labels: ['Projets en cours', 'Projets términés'],
               datasets: [{
                    data: [20, 80],
                    backgroundColor: ['#d2d6de', '#3c8dbc'],
                    borderColor: '#fff',
                    hoverOffset: 8
                }]
            },
            
            chartDataEvolutionMontant:{
              labels: ['Sécurité', 'Santé', 'Education', 'Agriculture'],
               datasets: [{
                    data: [20, 80, 35, 60],
                    hoverOffset: 8,
                },
                {data: [12, 44, 65, 78],
                    borderColor: '#43245',
                    hoverOffset: 8}
                    ]
            },

        }
    },
    methods: {
      getAnnee() {
        let annees = [];
        for (let index = 0; index < 5; index++) {
          annees.push(2022-index);
        }
        console.log(annees);
        return annees;
      }
  }

  }
</script>
