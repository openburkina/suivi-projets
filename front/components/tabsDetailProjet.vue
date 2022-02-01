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
          
          <TabInfoProjet :id="this.id"/>
        </v-tab-item>
        <v-tab-item value="tab-2">
          <TabActiviteProjet  :search="search" />
        </v-tab-item>
        <v-tab-item value="tab-3">
          <TabDecaissementProjet :search="search"/>
        </v-tab-item>
        <v-tab-item value="tab-4">
          <TabIndicateurProjet :search="search"/>
        </v-tab-item>
      </v-tabs-items>
    </v-card>
  </div>

</template>
<script>



export default {

  props: ['id'],
/* 
 async asyncData({store}){
      await Promise.all([
        store.dispatch('project/getProjectsData')
      ])
      return
     },
 computed:{
      ...mapState('project', {
        projets: state => state.projects,
        errors: state => state.errors,
      })
    },
 */
  data() {
    return {
      search: '',
      idProjet: this.$route.params.project_id,
      tab: null,
    }
  },
  /* 
  methods: {
    getTitle(message) {
      return `${message} sur le projet : ${this.idProjet}`
    },
    getProjet() {
      return this.projets.find((p) => p.project_id == this.idProjet)
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

   */
}
</script>
