<template>
  <v-card class="mx-auto" max-width="900">
    <Title value="Information sur le project" />
    <v-list-item>
      <v-list-item-title>ID</v-list-item-title>
      <v-list-item-subtitle>{{ project.project_id }}</v-list-item-subtitle>
    </v-list-item>
    <v-divider></v-divider>
    <v-list-item>
      <v-list-item-title>Titre</v-list-item-title>
      <v-list-item-subtitle>{{ project.title }}</v-list-item-subtitle>
    </v-list-item>
    <v-divider></v-divider>

    <v-list-item>
      <v-list-item-title>Bailleur</v-list-item-title>
      <v-list-item-subtitle>{{ project.org_name }}</v-list-item-subtitle>
    </v-list-item>
    <v-divider></v-divider>
    <v-list-item>
      <v-list-item-title>Exécutant</v-list-item-title>
      <v-list-item-subtitle>{{ project.operating_unit }}</v-list-item-subtitle>
    </v-list-item>
    <v-divider></v-divider>
    <v-list-item>
      <v-list-item-title>Secteur</v-list-item-title>
      <v-list-item-subtitle>{{ project.sector }}</v-list-item-subtitle>
    </v-list-item>
    <v-divider></v-divider>
    <v-list-item>
      <v-list-item-title>Région</v-list-item-title>
      <v-list-item-subtitle>{{ project.region }}</v-list-item-subtitle>
    </v-list-item>
    <v-divider></v-divider>
    <v-list-item>
      <v-list-item-title>Statut</v-list-item-title>
      <v-list-item-subtitle>
        <v-chip :color="getColor(project.activity_status)" dark>
          <v-icon size="24px">
            {{ getValue(project.activity_status) }}
          </v-icon>
        </v-chip>
      </v-list-item-subtitle>
    </v-list-item>
    <v-divider></v-divider>
    <v-list-item>
      <v-list-item-title>Budget</v-list-item-title>
      <v-list-item-subtitle>{{ project.budgetT }}</v-list-item-subtitle>
    </v-list-item>
    <v-divider></v-divider>

    <v-list-item>
      <v-list-item-title>Date de début</v-list-item-title>
      <v-list-item-subtitle>{{ project.start_date }}</v-list-item-subtitle>
    </v-list-item>
    <v-divider></v-divider>

    <v-list-item>
      <v-list-item-title>Date fin</v-list-item-title>
      <v-list-item-subtitle>{{ project.finish_date }}</v-list-item-subtitle>
    </v-list-item>
  </v-card>
</template>
<script>
import { mapState } from 'vuex'
export default {
  computed: {
    ...mapState('project', {
      project: (state) => state.project,
      errors: (state) => state.errors,
    }),
  },

  methods: {
    getColor(statut) {
      if (statut < 1) return '#00E396'
      else return '#008FFB'
    },
    getValue(statut) {
      if (statut < 1) return 'mdi-selection-ellipse'
      else return 'mdi-check'
    },
  },
}
</script>
