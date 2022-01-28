<template>
  <div>
    <Title value="Indicateurs du projet"></Title>
    <v-card class="mx-auto px-3">
      <v-data-table
        :headers="headersIndicateurs"
        :items="indicateurs"
        :search="search"
        class="elevation-0"
      >
        <!-- <template v-slot:[`item.statutCible`]="{ item }">
                <v-chip :color="getColor(item.statutCible)" dark>
                  <v-icon size="24px">
                    {{ getValue(item.statutCible) }}
                  </v-icon>
                </v-chip>
              </template> -->
      </v-data-table>
    </v-card>
  </div>
</template>
<script>
export default {
  props: ['search'],
  data() {
    return {
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
          statutCible: 1,
        },
        {
          id: 894,
          titre: 'IND 893',
          reference: 'KJD JJ NJD9',
          periodeRef: '2022-01-19',
          cible: '2022-02-27',
          periodeCible: '2021-12-19',
          statutCible: -1,
        },
      ],
    }
  },
}
</script>
