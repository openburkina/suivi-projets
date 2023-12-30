<template>
  <v-card>
    <v-card-title>
      {{title}}
      <v-spacer></v-spacer>
      <v-text-field
        v-model="search"
        solo
        append-icon="mdi-magnify"
        label="Search"
        single-line
        hide-details
        rounded
        
      ></v-text-field>
    </v-card-title>
    <v-data-table
      :headers="headers"
      :items=done
      :search="search"
      :items-per-page=5
      :options=
      "{sortBy: []}"
      :footer-props="{
        'items-per-page-text':'Activité'
      }"
      @click:row="createEditLink">
   
    </v-data-table>
  </v-card>
</template>

<script>
export default {
   props:{
     title:"",
     done:{
       type: []
     }
   },
  data(){
    return {
      search: '',
      items: [],
      annee:2018,
      select:null,

        headers: [
          {
            align: 'start',
            sortable: false,
            value: 'name',
          },
          { text: 'ID', value: 'identifiant' },
          { text: 'Nom', value: 'titre' },
          { text: 'Bailleur', value: 'bailleur' },
          { text: 'Secteur', value: 'secteur' },
          { text: 'Budget', value: 'montant' },
          { text: 'Date de Debut', value: 'datedebut' },
          { text: 'Date de Fin', value: 'datefin' },
          { text: 'Structure Executante', value: 'executant' },
        ],
    }
  },
  mounted(){
    for(this.annee;this.annee<2032;this.annee++){
      this.items.push(this.annee)
    }
  },
  computed:{},
  methods:{
    onChange(value){
     if(value.length!=0){
       console.log(this.$store.state.idRegion)
      //  this.$store.dispatch('',this.$store.state.idRegion)
     }
    },
    createEditLink(projet) {
      return this.$router.push({ path: '/projets/' + projet.identifiant})
    }
  }
}
</script>

