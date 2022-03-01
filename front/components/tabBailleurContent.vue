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
          <TabBailleurListeProjet :search="search"/>
        </v-tab-item>
        <v-tab-item value="tab-2">
          <Title :value="getTitle(`Stastistique`)"></Title>
          <v-card class="mx-auto px-3">
            <v-row>
              <v-col cols="6">
                <DonutChartStatutProjetParBailleur />
              </v-col>
              <v-col cols="6">
                <LineChartMontantParSecteurParBailleur />
              </v-col>
            </v-row>
            <v-row>
              <v-col cols="6">
                <BarChartMontantParBailleur />
              </v-col>
              <v-col cols="6">
                <BarChartMontantParSecteurParBailleur />
              </v-col>
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
      search: '',

      idBailleur: '-',
      tab: null,
    }
  },
  methods: {
    getTitle(message) {
      return `${message}  des projets sur la région : ${this.idBailleur}`
    },
    changeBailleur(a) {
      this.idBailleur = a
    },
  },
}
</script>
