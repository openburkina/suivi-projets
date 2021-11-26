<template>
  <v-card color="basil" style="width: 100%">
    <v-card-title class="text-center justify-center py-6">
      <h4 class="font-weight-bold basil--text">
        {{ project.project_id }} | {{ project.title }}
      </h4>
    </v-card-title>

    <v-tabs v-model="tab" background-color="transparent" color="basil" grow>
      <v-tab v-for="item in items" :key="item">
        {{ item }}
      </v-tab>
    </v-tabs>

    <v-tabs-items v-model="tab">
      <v-tab-item>
        <v-tab style="max-width: 100%">
          <!-- <v-text-field
            placeholder="Begining date"
            solo
            clearable class="mx-2"
          >
          </v-text-field>

          <v-text-field
            placeholder="Final date"
            solo
            clearable class="mx-2"
          >
          </v-text-field> -->

          <v-data-table
            dense
            :headers="headers"
            :items="activites"
            item-key="ID"
            class="elevation-1 my-4"
          ></v-data-table>
        </v-tab>
      </v-tab-item>
      <v-tab-item>
        <v-tab style="max-width: 100%">
          <v-data-table
            dense
            :headers="headers"
            :items="activites"
            item-key="ID"
            class="elevation-1 my-4"
          ></v-data-table>
        </v-tab>
      </v-tab-item>
      <v-tab-item>
        <v-tab style="max-width: 100%">
          <v-data-table
            dense
            :headers="headers"
            :items="activites"
            item-key="ID"
            class="elevation-1 my-4"
          ></v-data-table>
        </v-tab>
      </v-tab-item>
    </v-tabs-items>
  </v-card>
</template>
<script>
export default {
  data() {
    return {
      tab: null,
      items: ['Activities', 'Decaissement', 'Result'],
      text: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
      project: {
        project_id: '00089459',
        title: 'Funding Facility for Stabilization',
        description:
          'To quickly respond to immediate needs of the areas which were under Islamic State of Iraq and Levant (ISIL) control and facilitate the process of return of internally displaced persons, this project provides stabilization support in Iraq.',
        expense: 109578406,
        budget: 317860856,
        country: 'Iraq',
      },
      activites: [
        {
          ID: '10000129',
          Output: 'Donec vestibulum iaculis ullamcorper.',
          Theme: 'Responsive Institution',
          'Output Description': 'Country Name 5',
          Link: '$123,456,789',
        },
        {
          ID: '10000130',
          Output: 'Donec vestibulum iaculis ullamcorper.',
          Theme: 'Democratic Governance',
          'Output Description': 'Country Name 5',
          Link: '$123,456,789',
        },
      ],
      headers: [
        {
          text: 'ID',
          align: 'start',
          sortable: false,
          value: 'ID',
        },
        { text: 'Name', value: 'Output' },
        { text: 'Budget', value: 'Link' },
        { text: 'State', value: 'Theme' },
      ],
    }
  },
}
</script>
<style>
/* Helper classes */
.basil {
  background-color: #e4ecff !important;
}
.basil--text {
  color: #353868 !important;
}
</style>