<template>
  <v-container style="margin-top: -90px">
    <v-row>
      <v-col cols="4"> </v-col>
      <v-col cols="4" class="text-center">
        <div class="info--text font-weight-bold display-2 mx-auto">Donors</div>
        <hr
          style="
            height: 5px;
            background: #2196f3;
            border-color: #2196f3;
            border-radius: 10px;
          "
        />
      </v-col>
      <v-col cols="4"> </v-col>
    </v-row>

    <v-row>
      <Chips></Chips>
    </v-row>
    <v-row>
      <v-data-table
        dense
        :headers="headers"
        :items="bailleurs"
        item-key="name"
        class="elevation-1" style="width:100%"
      ></v-data-table>
    </v-row>
  </v-container>
</template>

<script>
export default {
  head() {
    return {
      title: "Donor's list",
    }
  },
  data: () => ({
    bailleurs: [
      {
        donor_name: 'United States of America',
        budget: '141135550',
        expense: '133113695',
        projects: '20',
        budget_sources: '05',
        'recipeint Offices': '05',
        share_percent: '30',
        point: '105',
        color: '#ff8500',
      },
      {
        donor_name: 'European Union',
        budget: '38323265',
        expense: '19016394',
        projects: '20',
        budget_sources: '05',
        'recipeint Offices': '05',
        share_percent: '15',
        point: '121',
        color: '#c8c607',
      },
      {
        donor_name: 'Japan',
        budget: '38323265',
        expense: '19016394',
        projects: '20',
        budget_sources: '05',
        'recipeint Offices': '05',
        share_percent: '10',
        point: '121',
        color: '#ff5640',
      },
      {
        donor_name: 'United Kingdom',
        budget: '38323265',
        expense: '19016394',

        projects: '20',
        budget_sources: '05',
        'recipeint Offices': '05',
        share_percent: '25',
        point: '121',
        color: '#69b13a',
      },
      {
        donor_name: 'Norway',
        budget: '38323265',
        expense: '19016394',

        projects: '20',
        budget_sources: '05',
        'recipeint Offices': '05',
        share_percent: '12',
        point: '121',
        color: '#029fd9',
      },
      {
        donor_name: 'Sweden',
        budget: '38323265',
        expense: '19016394',

        projects: '20',
        budget_sources: '05',
        'recipeint Offices': '05',
        share_percent: '5',
        point: '121',
        color: '#d9d73a',
      },
      {
        donor_name: 'Canada',
        budget: '38323265',
        expense: '19016394',

        projects: '20',
        budget_sources: '05',
        'recipeint Offices': '05',
        share_percent: '3',
        point: '121',
        color: '#993399',
      },
      {
        donor_name: 'Germany',
        budget: '38323265',
        expense: '19016394',

        projects: '20',
        budget_sources: '05',
        'recipeint Offices': '05',
        share_percent: '3',
        point: '121',
        color: '#ff8500',
      },
      {
        donor_name: 'France',
        budget: '38323265',
        expense: '19016394',

        projects: '20',
        budget_sources: '05',
        'recipeint Offices': '05',
        share_percent: '3',
        point: '121',
        color: '#c8c607',
      },
    ],
    headers: [
      {
        text: 'Name',
        align: 'start',
        sortable: false,
        value: 'donor_name',
      },
      { text: 'Budget', value: 'budget' },
      { text: 'Expense', value: 'expense' },
    ],
  }),
}
</script>

