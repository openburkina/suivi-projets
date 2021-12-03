<template>
  <div >

    <v-card>
      <v-card-title>
        <v-text-field
          v-model="search"
          append-icon="mdi-magnify"
          label="Search"
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
            <v-toolbar-title>Donors List</v-toolbar-title>
            <v-divider
              class="mx-4"
              inset
              vertical
            ></v-divider>
            <v-spacer></v-spacer>

            <v-btn
              color="primary"
              dark
              class="mb-2"
              @click="dialog.mode='Register New', dialog.show='true'"
            >
              New Donor
            </v-btn>
          </v-toolbar>
        </template>
          <template slot="items" slot-scope="props">
          <td class="text-xs-center">{{props.index}}</td>
          <td class="text-xs-center">{{props.item.name}}</td>
          <td class="text-xs-center">{{props.item.description}}</td>
        </template>
                  <template v-slot:item.actions="{ item }">
                    <v-icon
                      medium
                      color="primary"
                      class="mr-2"
                      @click="onEdit(item)"
                    >
                      mdi-pencil
                    </v-icon>
                    <v-icon
                      medium
                      color="red"
                      @click="onDelete(item.id)"
                    >
                      mdi-delete
                    </v-icon>
                  </template>
      </v-data-table>
    </v-card>
    <v-layout row justify-center>
      <dialogdonor :mode="dialog.mode" :show.sync="dialog.show" @closedialog="onClose"
      ></dialogdonor>
    </v-layout>
  </div>
</template>

<script>

  import {mapGetters, mapState, mapActions} from 'vuex'
  import dialogdonor from '././donor/add'

  export default {
  
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
            text: 'Name',
            align: 'start',
            value: 'name',
          },
          { text: 'Description', value: 'description' },
          { text: 'Actions', value: 'actions', sortable: false },
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
    components:{
       'dialogdonor': dialogdonor,
    },
  }
</script>