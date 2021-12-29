<template>
  <div>
          <v-card>
      <v-card-title>
        <v-text-field
          v-model="search"
          append-icon="mdi-magnify"
          label="Rechercher"
          single-line
          hide-details
        ></v-text-field>
      </v-card-title>
      <v-data-table
        :headers="headers"
        :items="projects"
        sort-by="Name"
        :search="search"
        class="elevation-1"
      >
        <template v-slot:top>
          <v-toolbar
            flat
          >
            <v-toolbar-title>Liste des Projets</v-toolbar-title>
            <v-divider
              class="mx-4"
              inset
              vertical
            ></v-divider>
            <v-spacer></v-spacer>
          </v-toolbar>
        </template>

           <template slot="items" slot-scope="props">
           <td class="text-xs-center">{{props.item.created_at}}</td>
          <td class="text-xs-center">{{props.item.title}}</td>
          <td class="text-xs-center">{{props.item.country}}</td>
          <td class="text-xs-center">{{props.item.budget}}</td>
          <td class="text-xs-center">{{props.item.expense}}</td>
          <td class="text-xs-center">{{props.item.organisation}}</td> 
          <td class="text-xs-center">{{props.item.activity_status}}</td>
          <td class="text-xs-center">{{props.item.description}}</td> 
         
        </template>
                 
      </v-data-table>
    </v-card>
	

  </div>
</template>

<script>
  import {mapGetters, mapState, mapActions} from 'vuex'

export default {
layout: 'page-layout',

async asyncData({store}){
      await Promise.all([
        store.dispatch('project/getProjectsData')
      ])
      return
    },

    data: () => ({
      dialog: {
        show: false,
        mode: '',
      },
      search: '',
      headers: [
        { text: 'Date', value: 'created_at' },
        {
          text: 'Libelé',
          align: 'start',
          value: 'title',
        },
        { text: 'Pays', value: 'country' },
        { text: 'Budget', value: 'budget' },
        { text: 'Dépenses', value: 'expense' },
        { text: 'Organisation', value: 'organisation' },
        { text: 'Status', value: 'activity_status' },
        { text: 'Description', value: 'description', width: '450px'},
        
      ],
    }),

       methods: {
      onClose(param){
       // alert(param)
        this.dialog.show = param
      },
     ...mapActions('project', ['destroyProjectData', 'formEditDate', ]),
      onDelete(param){
        alert(param)
        this.destroyProjectData(param)
      },

      
    },
        computed:{
      ...mapState('project', {
        projects: state => state.projects,
        errors: state => state.errors,
      })
    },
}
</script>
