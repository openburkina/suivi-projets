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
          item-text="name"
          item-value="region_code"
          bottom
          autocomplete
          v-on:change="changeRegion"
        >
        </v-select>
      </v-tabs>

      <v-tabs-items v-model="tab" class="mb-9">
        <v-tab-item value="tab-1" class="mb-9">
          <TabRegionListeProjet :search="search"/>
        </v-tab-item>
        <v-tab-item value="tab-2">
          <Title :value="getTitle(`Stastistique`)"></Title>
          <v-card class="mx-auto px-3">
            <v-row>
              <v-col cols="6">
                <DonutChartStatutProjetParRegion />
              </v-col>
              <v-col cols="6">
                <LineChartMontantParSecteurParRegion />
              </v-col>
            </v-row>
            <v-row>
              <v-col cols="6">
                <BarChartMontantParRegionParRegion />
              </v-col>
              <v-col cols="6">
                <BarChartMontantParSecteurParRegion />
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
  props: {
    regions: Array,
  },
  data() {
    return {
      region: null,
      // regions: [
      //   { id: '1111', nom: 'BAI 1' },
      //   { id: '2222', nom: 'BAI 2' },
      //   { id: '3333', nom: 'BAI 3' },
      // ],
      search: '',

      idRegion: '-',
      tab: null,
    }
  },
  methods: {
    getTitle(message) {
      return `${message}  des projets sur la région : ${this.idRegion}`
    },
    changeRegion(a) {
      this.idRegion = a
    },
  },
}
</script>
