<template>
  <div>
    <Title value="Décaissements du projet"></Title>
    <v-card class="mx-auto px-3">
      <v-data-table
        :headers="headersDecaissements"
        :items="decaissements"
        :search="search"
        class="elevation-0"
      >
      </v-data-table>
    </v-card>
  </div>
</template>
<script>
export default {
  props: ['search'],
  data() {
    return {
      
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
    }
  },
}
</script>
