<template>
  <div>
    <Title value="Liste des projets de la région"></Title>
    <v-card class="mx-auto px-3">
      <v-data-table :headers="headersProjets" :items="projets" :search="search">
      </v-data-table>
    </v-card>
  </div>
</template>
<script>
export default {
  props:['search'],
  data() {
    return {
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
    }
  },
}
</script>
