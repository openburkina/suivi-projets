 <template>        
         
         <v-menu
        bottom
        origin="center center"
        transition="fab-transition"
        nudge-bottom="30"
        open-on-hover :close-on-content-click="false"
      >

        <template v-slot:activator="{ on, attrs }">
          <v-btn
          text
          class="#21618C--text"
            v-bind="attrs"
            v-on="on"
          >
           Projets
          <v-icon class="ml-4"> mdi-chevron-down</v-icon>
          </v-btn>
        </template>
        <v-card>
          <v-list-item-content class="justify-center">
            <div class="mx-auto text-center">
             
              <v-btn
                depressed
                text
                to="/projects"
              >
                <v-icon class="mx-3">
                  mdi-thumb-up-outline
                </v-icon>
                <span class="mx-2">
                  Projets par Bailleur
                </span>
              </v-btn>

              
              <v-divider class="my-3"></v-divider>
              <v-btn
                depressed
                text
                to="/projects1"
              >
              <v-icon class="mx-3">
                mdi-thumb-up
              </v-icon>
              <span class="mx-2">Projets réalisés par Bailleur </span>
                
              </v-btn>


           
              <v-divider class="my-3"></v-divider>
              <v-btn
                depressed
                text
                to="/projects2"
              >
              <v-icon class="mx-3">
                mdi-thumb-up
              </v-icon>
              <span class="mx-2">Projets Ordonnés par bailleur </span>
                
              </v-btn>


              <v-divider class="my-3"></v-divider>
              <v-btn
                depressed
                text
                to="/projects3"
              >
              <v-icon class="mx-3">
                mdi-thumb-up
              </v-icon>
              <span class="mx-2">Projets par Region </span>
                
              </v-btn>



            </div>
          </v-list-item-content>
        </v-card>

      </v-menu>
</template>

<script>
export default {

}
</script>
