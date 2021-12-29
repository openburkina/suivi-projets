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
        :items="backers"
        sort-by="Name"
        :search="search"
        class="elevation-1"
      >
        <template v-slot:top>
          <v-toolbar
            flat
          >
            <v-toolbar-title>Liste des Bailleurs</v-toolbar-title>
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
          <td class="text-xs-center">{{props.item.project}}</td>
          <td class="text-xs-center">{{props.item.budget}}</td>
          <td class="text-xs-center">{{props.item.organisation}}</td>
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
          store.dispatch('donor/getDonorsData')
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
            value: 'project',
          },
          { text: 'Organisation', value: 'organisation' },
          { text: 'Budget', value: 'budget' },
        ],
      }
    },

    methods: {
      onClose(param){
       // alert(param)
        this.dialog.show = param
      },
     ...mapActions('donor', ['destroyDonorData']),
        onDelete(param){
        alert(param)
        this.destroyDonorData(param)
      },

      onEdit(param){
        // alert("Edit Donor with ID: " + param)
        this.dialog.mode = 'Edit'
        this.dialog.show = true
         // alert(param.name)
      }
    },

    computed:{
      ...mapState('donor', {
        backers: state => state.donors,
        errors: state => state.errors,
      })
    },
}
</script>
