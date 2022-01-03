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
        :items="projects3"
        sort-by="Name"
        :search="search"
        class="elevation-1"
      >
        <template v-slot:top>
          <v-toolbar
            flat
          >
            <v-toolbar-title>Liste des Projets Ordonnés par bailleur</v-toolbar-title>
            <v-divider
              class="mx-4"
              inset
              vertical
            ></v-divider>
            <v-spacer></v-spacer>
          </v-toolbar>
        </template>
          <template slot="items" slot-scope="props">
          <td class="text-xs-center">{{props.id}}</td>
          <td class="text-xs-center">{{props.item.title}}</td>
          <td class="text-xs-center">{{props.item.organisation}}</td>
          <td class="text-xs-center">{{props.item.operating_unit}}</td>
          <td class="text-xs-center">{{props.item.activity_status}}</td>
        </template>
      </v-data-table>
    </v-card>

  </div>
</template>

<script>
  import {mapState} from 'vuex'

export default {
layout: 'page-layout',

async asyncData({store}){
      await Promise.all([
          store.dispatch('project3/getSect_AggregateData')
      ])
      return
    },

        data(){
    return{
      dialog: {
            show: false,
            mode: '',
        },
        search: '',
        headers: [
        { text: 'No.', value: 'id' },
          {
            text: 'Projet',
            align: 'start',
            value: 'title',
          },
          { text: 'Organisation', value: 'organisation' },
          { text: 'Unite d\'Operation', value: 'operating_unit'},
          { text: 'Status', value: 'activity_status' },
        ],
      }
    },

    computed:{
      ...mapState('project3', {
        projects3: state => state.projects3,
        errors: state => state.errors,
      })
    },
}
</script>
