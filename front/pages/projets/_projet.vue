<template>
  <div>
      <v-tabs
        v-model="tab"
        background-color="indigo lighten-5"
        centered
        icons-and-text
      >
        <v-tabs-slider></v-tabs-slider>

        <v-tab href="#tab-1">
          Infos
          <v-icon>mdi-axis-arrow-info</v-icon>
        </v-tab>

        <v-tab href="#tab-2">
           Activités
           <v-icon>mdi-format-list-text</v-icon>
        </v-tab>

        <v-tab href="#tab-3">
          Décaissement
          <v-icon>mdi-cash</v-icon>
        </v-tab>

        <v-tab href="#tab-4">
           Indicateurs
          <v-icon>mdi-chart-timeline</v-icon>
        </v-tab>

      </v-tabs>

      <v-tabs-items v-model="tab" class="mb-9">
        <v-tab-item value="tab-1" class="mb-9">
          <ProjectInfo :info="info" />
        </v-tab-item>
        <v-tab-item value="tab-2">
          <ProjectChild  :search="search"  :items="childs"/>
        </v-tab-item>
        <v-tab-item value="tab-3">
          <ProjectTransaction  :search="search"  :items="transactions"/>
        </v-tab-item>
        <v-tab-item value="tab-4">
          <ProjectIndicateur  :search="search"  :items="indicateurs"/>
        </v-tab-item>

      </v-tabs-items>
  </div>
</template>
<script>
  import { mapState, mapActions } from 'vuex';

  export default {
    data() {
      return {
        id: this.$route.params.projet,
        search: '',
        tab: null,
      }
    },
    computed: {
      ...mapState({
        info: 'projectDetails',
        childs: 'projectDetailsChild',
        transactions: 'projectDetailsTransaction',
        indicateurs :'projectDetailsIndicateur',
        
      })
    },

    async mounted() {
      this.fetchProjectsDetails(this.id);
      this.fetchProjectsDetailsChild(this.id);
      this.fetchProjectsDetailsTransaction(this.id);
      this.fetchProjectsDetailsIndicateur(this.id);
/*       setTimeout(() => ,500);
      setTimeout(() => ,500);
      setTimeout(() => ,500);
      setTimeout(() => ,500); */
        },
    methods: {
      ...mapActions([
        'fetchProjectsDetails',
        'fetchProjectsDetailsTransaction',
        'fetchProjectsDetailsIndicateur',
        'fetchProjectsDetailsChild',
  ]),
      getTitle(message) {
        return `${message} sur le projet : ${this.id}`
      },
      getProjet() {
        return this.projets.find((p) => p.id == this.id)
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