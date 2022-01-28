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
          label="Selectionnez un bailleur"
          item-text="org_name"
          item-value="ref_id"
          bottom
          autocomplete
          v-on:change="changeBailleur"
        >
        </v-select>
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
                <BarChartMontantParRegionParBailleur />
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
   props: {
    bailleurs: Array,
  },
  data() {
    return {
      bailleur: null,
      // bailleurs: [
      //   { id: '1111', nom: 'BAI 1' },
      //   { id: '2222', nom: 'BAI 2' },
      //   { id: '3333', nom: 'BAI 3' },
      // ],
      search: '',

      idBailleur: '-',
      tab: null,
    }
  },
  methods: {
    getTitle(message) {
      return `${message}  des projets sur le bailleur : ${this.idBailleur}`
    },
    getColor(statut) {
      if (statut < 1) return '#00E396'
      else return '#008FFB'
    },
    getValue(statut) {
      if (statut < 1) return 'mdi-close'
      else return 'mdi-check'
    },
    changeBailleur(a) {
      this.idBailleur = a
    },
  },
}
</script>
