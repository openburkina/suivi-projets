<template>
  <v-app>
    <v-navigation-drawer
      v-model="drawer"
      :mini-variant="miniVariant"
      app
      fixed
      temporary
      color="indigo lighten-1"
    >
      <v-list>
        <v-list-item>
          <v-list-item-content>
              <img
                :src="require('~/assets/img/pnud.png')" height="100"
              >
          </v-list-item-content>
        </v-list-item>
      </v-list>

      <v-divider />

      <v-list
        nav
        dense
      >
        <v-list-item-group
          active-class="white--text"
        >
          <v-list-item to="/">
            <v-list-item-icon>
              <v-icon>mdi-home</v-icon>
            </v-list-item-icon>
            <v-list-item-title>Accueil</v-list-item-title>
          </v-list-item>

          <v-list-item to="/projets">
            <v-list-item-icon>
              <v-icon>mdi-menu</v-icon>
            </v-list-item-icon>
            <v-list-item-title>Projets</v-list-item-title>
          </v-list-item>
          
          <v-list-item to="/bailleurs">
            <v-list-item-icon>
              <v-icon>mdi-menu</v-icon>
            </v-list-item-icon>
            <v-list-item-title>Bailleurs</v-list-item-title>
          </v-list-item>
          
          <v-list-item to="/regions">
            <v-list-item-icon>
              <v-icon>mdi-menu</v-icon>
            </v-list-item-icon>
            <v-list-item-title>R&eacute;gions</v-list-item-title>
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>



    <v-app-bar
      app
      fixed
      height="90"
      v-bind:elevation="scrollPosition>28?4:0"
      color="indigo lighten-1"
    >
        <img
          :src="require('~/assets/img/logo.png')" class="logo"
        >
  
      <v-spacer />
      <v-app-bar-nav-icon
        v-if="isXs"
        class="ml-2"
        color="white"
        @click.stop="drawer = !drawer"
      />

      <div v-else>
        <v-btn to="/" text>
          <span class="mr-2 #21618C--text">Accueil</span>
        </v-btn>
        <v-btn text to="/projets">
          <span class="mr-2  #21618C --text">Projets</span>
        </v-btn>
        <v-btn text to="/bailleurs">
          <span class="mr-2  #21618C --text">Bailleurs</span>
        </v-btn>
        <v-btn text to="/regions">
          <span class="mr-2  #21618C --text">R&eacute;gions</span>
        </v-btn>
      </div>
    </v-app-bar>
    <v-main>
      <v-container fluid>
       <Nuxt />
      </v-container>
          <Footer />
    </v-main>
    <v-scale-transition>
      <v-btn
        v-scroll="onScroll"
        v-show="fab"
        fab
        dark
        fixed
        bottom
        right
        color="indigo lighten-1"
        @click="toTop"
        elevation="10"
      >
        <v-icon>mdi-arrow-up</v-icon>
      </v-btn>
    </v-scale-transition>
  </v-app>
</template>

<script>
export default {
  data: () => ({
    drawer: null,
    isXs: false,
    miniVariant:false,
    fab: false,
    scrollPosition: null,

  }),
  watch: {
    isXs(value) {
      if (!value) {
        if (this.drawer) {
          this.drawer = false;
        }
      }
    },
    
  },
  
 
  mounted() {
    this.onResize();
    window.addEventListener("resize", this.onResize, { passive: true });
    window.addEventListener('scroll', this.updateScroll);

  },
   methods: {
    onResize() {
      this.isXs = window.innerWidth < 850;
    },
    updateScroll() {
       this.scrollPosition = window.scrollY
    },
    onScroll (e) {
      if (typeof window === 'undefined') return
      const top = window.pageYOffset ||   e.target.scrollTop || 0
      this.fab = top > 20
    },
    toTop () {
      this.$vuetify.goTo(0)
    }
  },
  
};
</script>
<style scoped>
.v-toolbar {
  transition: 0.6s;
}
active-class{
  color:red;
}

.v-btn{
  z-index:999;
}
.logo{
  width: 60px;
  height: 90px;
}
</style>

