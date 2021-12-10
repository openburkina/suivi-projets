<template>
  <div>

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
            <v-toolbar-title>Project List</v-toolbar-title>
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
              New Project
            </v-btn>
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
                  <template v-slot:item.actions="{ item }">
                    <v-icon
                      medium
                      color="primary"
                      class="mr-2"
                      @click="onEdit(item.id)"
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

    filters: {
  truncate(string, value) {
    return string.substring(0, value) + '…';
  }
},

    async asyncData({store}){
      await Promise.all([
        store.dispatch('project1/getProjectsData')
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
          text: 'Title',
          align: 'start',
          value: 'title',
          width: '250px',
        },
        { text: 'Country', value: 'country' },
        { text: 'Budget', value: 'budget' },
        { text: 'Expense', value: 'expense' },
        { text: 'Organisation', value: 'organisation' },
        { text: 'Status', value: 'activity_status' },
        { text: 'Description', value: 'description', width: '450px'},
        { text: 'Actions', value: 'actions', sortable: false , width: '150px'},
      ],
    }),

    methods: {
      onClose(param){
       // alert(param)
        this.dialog.show = param
      },
     ...mapActions('project1', ['destroyProjectData', 'formEditDate', ]),
      onDelete(param){
        alert(param)
        this.destroyProjectData(param)
      },

      onEdit(param){
        alert("Edit Donor with ID: " + param)
/* 
        this.formEditDate(param)
        this.$store.state.toolbarActions
        this.dialog.mode = 'Edit'
        this.dialog.show = true
         */
      }
      
    },

    computed:{
      ...mapState('project1', {
        backers: state => state.projects,
        errors: state => state.errors,
      })
    },
    components:{
       'dialogdonor': dialogdonor,
    },
  }
</script>
