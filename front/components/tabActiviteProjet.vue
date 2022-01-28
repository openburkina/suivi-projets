<template>
  <v-card class="mx-auto px-3">
    <Title value="Activités sur le projet" />
    <v-data-table
      :headers="headers"
      :items="activites"
      :search="search"
      class="elevation-0"
    >
      <!-- <template v-slot:[`item.statut`]="{ item }">
        <v-chip :color="this.getColor1(item.statut)" dark>
          <v-icon size="24px">
            {{ this.getValue1(item.statut) }}
          </v-icon> 
        </v-chip>
      </template> -->
    </v-data-table>
     <!-- <h2>{{this.getColor1(1)}},{{this.getValue1(1)}}</h2>  -->
  </v-card>
</template>
<script>
export default {
  props: ['search'],
  data() {
    return {
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
    }
  },
}
</script>
