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
          Info
          <v-icon>mdi-axis-arrow-info</v-icon>
        </v-tab>

        <v-tab href="#tab-2">
          Activités
          <v-icon>mdi-archive</v-icon>
        </v-tab>

        <v-tab href="#tab-3">
          Décaissements
          <v-icon>mdi-bank</v-icon>
        </v-tab>

        <v-tab href="#tab-4">
          Indicateurs
          <v-icon>mdi-arrow-projectile</v-icon>
        </v-tab>
      </v-tabs>

      <v-tabs-items v-model="tab" class="mb-9">
        <v-tab-item value="tab-1" class="mb-9">
          <Title :value="getTitle(`Info`)"></Title>
          <v-card class="mx-auto" max-width="900">
            <v-list-item>
              <v-list-item-title>ID</v-list-item-title>
              <v-list-item-subtitle>{{ getProjet().id }}</v-list-item-subtitle>
            </v-list-item>
            <v-divider></v-divider>
            <v-list-item>
              <v-list-item-title>Bailleur</v-list-item-title>
              <v-list-item-subtitle>{{
                getProjet().bailleur
              }}</v-list-item-subtitle>
            </v-list-item>
            <v-divider></v-divider>
            <v-list-item>
              <v-list-item-title>Exécutant</v-list-item-title>
              <v-list-item-subtitle>{{
                getProjet().executant
              }}</v-list-item-subtitle>
            </v-list-item>
            <v-divider></v-divider>
            <v-list-item>
              <v-list-item-title>Secteur</v-list-item-title>
              <v-list-item-subtitle>{{
                getProjet().secteur
              }}</v-list-item-subtitle>
            </v-list-item>
            <v-divider></v-divider>
            <v-list-item>
              <v-list-item-title>Région</v-list-item-title>
              <v-list-item-subtitle>{{
                getProjet().région
              }}</v-list-item-subtitle>
            </v-list-item>
            <v-divider></v-divider>
            <v-list-item>
              <v-list-item-title>Statut</v-list-item-title>
              <v-list-item-subtitle>{{
                getProjet().statut
              }}</v-list-item-subtitle>
            </v-list-item>
            <v-divider></v-divider>
            <v-list-item>
              <v-list-item-title>Budget</v-list-item-title>
              <v-list-item-subtitle>{{
                getProjet().budget
              }}</v-list-item-subtitle>
            </v-list-item>
            <v-divider></v-divider>
            <v-list-item>
              <v-list-item-title
                >Date de dernière mise à jour</v-list-item-title
              >
              <v-list-item-subtitle>{{
                getProjet().dateDerniereMAJ
              }}</v-list-item-subtitle>
            </v-list-item>
          </v-card>
        </v-tab-item>
        <v-tab-item value="tab-2">
          <Title :value="getTitle(`Activités`)"></Title>
          <v-card class="mx-auto px-3">
            <v-data-table
              :headers="headers"
              :items="activites"
              :search="search"
              class="elevation-0"
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
        </v-tab-item>
        <v-tab-item value="tab-3">
          <Title :value="getTitle(`Décaissement`)"></Title>
          <v-card class="mx-auto px-3">
            <v-data-table
              :headers="headersDecaissements"
              :items="decaissements"
              :search="search"
              class="elevation-0"
            >
            </v-data-table>
          </v-card>
        </v-tab-item>
        <v-tab-item value="tab-4">
          <Title :value="getTitle(`Indicateur`)"></Title>
          <v-card class="mx-auto px-3">
            <v-data-table
              :headers="headersIndicateurs"
              :items="indicateurs"
              :search="search"
              class="elevation-0"
            >
            <template v-slot:[`item.statutCible`]="{ item }">
          <v-chip :color="getColor(item.statutCible)" dark>
            <v-icon size="24px">
              {{ getValue(item.statutCible) }}
            </v-icon>
          </v-chip>
        </template>
            </v-data-table>
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
      headersIndicateurs: [
        {
          text: 'ID',
          align: 'start',
          sortable: false,
          value: 'id',
        },
        { text: 'Titre', value: 'titre' },
        { text: 'Référence', value: 'reference' },
        { text: 'Période référence', value: 'periodeRef' },
        { text: 'Cible', value: 'cible' },
        { text: 'Période Cible', value: 'periodeCible' },
        { text: 'Statut Cible', value: 'statutCible' },
      ],
      indicateurs: [
        {
          id: 7466,
          titre: 'IND 348',
          reference: 'IND JJ CD98',
          periodeRef: '2021-12-19',
          cible: '2022-01-19',
          periodeCible: '2021-12-19',
          statutCible: 1
        },
        {
          id: 894,
          titre: 'IND 893',
          reference: 'KJD JJ NJD9',
          periodeRef: '2022-01-19',
          cible: '2022-02-27',
          periodeCible: '2021-12-19',
          statutCible: -1
        },
      ],
      headersDecaissements: [
        {
          text: 'ID',
          align: 'start',
          sortable: false,
          value: 'id',
        },
        { text: 'Date', value: 'date' },
        { text: 'Montant', value: 'montant' },
        { text: 'Livrable', value: 'livrable' },
      ],
      decaissements: [
        {
          id: 11110,
          livrable: '2022-01-19',
          montant: 12849585.94,
          date: '2021-12-19',
        },
        {
          id: 3221,
          livrable: '2022-01-19',
          montant: 12849585.94,
          date: '2021-12-19',
        },
        {
          id: 543,
          livrable: '2022-01-19',
          montant: 12849585.94,
          date: '2021-12-19',
        },
      ],
      headers: [
        {
          text: 'ID',
          align: 'start',
          sortable: false,
          value: 'id',
        },
        { text: 'Titre', value: 'titre' },
        { text: 'Date début', value: 'dateDebut' },
        { text: 'Date fin', value: 'dateFin' },
        { text: 'Montant', value: 'montant' },
        { text: "Acteurs d'éxecutions", value: 'acteurExc' },
        { text: 'Acteurs partenaires', value: 'acteurPart' },
        { text: 'Statut', value: 'statut' },
        { text: 'Année de planifications', value: 'anneePlan' },
      ],
      activites: [
        {
          id: 11110,
          statut: 1,
          titre: 'ACT 878CC',
          dateDebut: '2021-12-12',
          dateFin: '2022-01-07',
          montant: 12849585.94,
          acteurExc: 'EXC LLC',
          acteurPart: 'PRT 987',
          anneePlan: '2021-12-11',
        },
        {
          id: 11122,
          statut: -1,
          titre: 'ACT UJI87',
          dateDebut: '2021-12-19',
          dateFin: '2022-01-07',
          montant: 12777785.94,
          acteurExc: 'EXC MLC',
          acteurPart: 'PRT 543',
          anneePlan: '2021-12-11',
        },
        {
          id: 11133,
          statut: -1,
          titre: 'ACT MN88',
          dateDebut: '2021-12-10',
          dateFin: '2022-01-07',
          montant: 12777785.94,
          acteurExc: 'EXC MLC',
          acteurPart: 'PRT 943',
          anneePlan: '2021-12-11',
        },
      ],
      idProjet: this.$route.params.id,
      tab: null,
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
    getTitle(message) {
      return `${message} sur le projet : ${this.idProjet}`
    },
    getProjet() {
      return this.projets.find((p) => p.id == this.idProjet)
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
