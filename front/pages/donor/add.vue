<template>
  <div>

    <v-dialog
      v-model="dialog.show"
      persistent
      max-width="600px"
    >
      <v-card>
        <v-card-title>
          <span class="heading">{{dialog.mode}} Donor</span>
        </v-card-title>
        <v-card-text>

          <v-layout wrap row>
            <v-flex xs12>
              <v-text-field
                v-model="form.name"
                label="Name*"
                required
              ></v-text-field>
              <v-text-field
                v-model="form.description"
                label="Description*"
                required
              ></v-text-field>
            </v-flex>
          </v-layout>

        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="blue darken-1"
            text
            @click.native="onClose"
          >
            Close
          </v-btn>
          <v-btn
            color="blue darken-1"
            text
            @click.native="submit"
          >
            Save
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
  import {mapActions, mapState} from 'vuex'
  export default {
    props: ['show', 'mode'],
    data(){
      return{
        dialog: {
          show: false,
          mode: '',
        },
        form: {
          id: 0,
          name: '',
          description: '',
        }
      }
    },
    watch:{
      show(param){
        this.dialog.show = param
      },

     mode(param){
        this.dialog.mode = param
        if(param === 'Edit'){
          if(this.formEdit.id === 0){
            return
          }else {

              this.form.id = this.formEdit.id
              this.form.name = this.formEdit.name
              this.form.description = this.formEdit.description
               
              // alert(this.$store.DONOR_MODULE.formEdit)
          }
        }
      }
    },
    methods:{
      ...mapActions('donor', ['storeDonorsData', 'updateDonorData']),
      submit(){
        if (this.mode === 'Edit'){
          let param = {
            name: this.form.name,
            description:  this.form.description,
          }
          let data = Object.assign({id: this.form.id}, param)
          this.updateBakerData(data).then(()=> this.$router.push({name: 'donors'}))
          this.clearForm()
          this.$emit("closedialog", false)
          this.dialog.show = false
        }else {
          let param = {
            name: this.form.name,
            description:  this.form.description,
          }
          this.storeDonorsData(param).then(()=> this.$router.push({name: 'donors'}))
          this.clearForm()
          this.$emit("closedialog", false)
          this.dialog.show = false
     }

      },
      onClose(){
        this.$emit("closedialog", false)
        this.dialog.show = false
        this.clearForm()
        //this.$router.push({name: ''})
      },
      clearForm(){
        this.form.name = ""
        this.form.description = ""
      },
    },

    computed:{
        ...mapState('donor', {
          formEdit: state => state.formEdit
        }),
      formData () {
        return this.$store.state.formEdit
      }
    },

  }
</script>
