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
      </v-tabs>

      <v-tabs-items v-model="tab" class="mb-9">
        <v-tab-item value="tab-1" class="mb-9">
          <Title :value="titleList"></Title>
          <TabBailleurListeProjet :search="search"/>
        </v-tab-item>
        <v-tab-item value="tab-2">
           <Title :value="titleStatistique" />
          <v-row class="px-3 py-3">
            <v-col cols="6">
              <v-card class="mx-auto">
                <v-card-title class="text-h5">Statut des projets</v-card-title>
                <v-card-subtitle
                  >Pourcentage des projes t&eacute;rmin&eacute;s et en
                  cours</v-card-subtitle
                >
                <v-divider></v-divider>
                <DonutChartStatutProjetParBailleur />
              </v-card>
            </v-col>
            <v-col cols="6">
              <v-card class="mx-auto">
                <v-card-title class="text-h5"
                  >Montant par secteurs</v-card-title
                >
                <v-card-subtitle
                  >Evolutions des montants par secteurs</v-card-subtitle
                >
                <v-divider></v-divider>
                <LineChartMontantParSecteurParBailleur />
              </v-card>
            </v-col>
          </v-row>
          <v-row class="px-3 py-3">
            <v-col cols="6"
              ><v-card class="mx-auto">
                <v-card-title class="text-h5"
                  >Montant par regions</v-card-title
                >
                <v-card-subtitle
                  >Montant des projets par regions</v-card-subtitle
                >
                <v-divider></v-divider>
                <BarChartMontantParBailleurParBailleur /> </v-card
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
                <BarChartMontantParSecteurParBailleur /> </v-card
            ></v-col>
          </v-row>
        </v-tab-item>
      </v-tabs-items>
    </v-card>
  </div>
</template>
<script>

import { mapState } from 'vuex'

export default {
  data() {
    return {
      search: '',

      idBailleur: '-',
      tab: null,
    }
  },
  methods: {
    getTitle(message) {
      return `${message}  des projets sur la bailleur : ${this.idBailleur}`
    },
    changeBailleur(a) {
      this.idBailleur = a
    },
  },
  computed: {
    ...mapState('bailleur', {
      titleList: (state) => `Liste des projets du bailleur : ${state.name}`,
      titleStatistique: (state) =>
        `Statistiques des projets du bailleur : ${state.name}`,
    }),
  },
}
</script>
