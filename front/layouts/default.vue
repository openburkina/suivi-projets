<template>
  <v-app>
    <Caroussel />

    <v-navigation-drawer
      v-model="drawer"
      :mini-variant="miniVariant"
      app
      fixed
      temporary
    >
      <MenuSide/>
    </v-navigation-drawer>

    <v-app-bar
      app
      fixed
      height="90"
      v-bind:elevation="scrollPosition > 28 ? 4 : 0"
      v-bind:color="scrollPosition < 28 ? 'transparent' : 'indigo lighten-1'"
      dark
    >
      <img :src="require('~/assets/img/logo.png')" height="60" width="50" />

      <v-spacer />
      <v-app-bar-nav-icon
        v-if="isXs"
        class="ml-2"
        color="white"
        @click.stop="drawer = !drawer"
      />

      <div v-else>
        <MenuNavbar />
      </div>
    </v-app-bar>
    <v-main>
      <v-container>
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
    miniVariant: false,
    fab: false,
    scrollPosition: null,
  }),
  watch: {
    isXs(value) {
      if (!value) {
        if (this.drawer) {
          this.drawer = false
        }
      }
    },
  },

  mounted() {
    this.onResize()
    window.addEventListener('resize', this.onResize, { passive: true })
    window.addEventListener('scroll', this.updateScroll)
  },
  methods: {
    onResize() {
      this.isXs = window.innerWidth < 850
    },
    updateScroll() {
      this.scrollPosition = window.scrollY
    },
    onScroll(e) {
      if (typeof window === 'undefined') return
      const top = window.pageYOffset || e.target.scrollTop || 0
      this.fab = top > 20
    },
    toTop() {
      this.$vuetify.goTo(0)
    },
  },
}
</script>
<style scoped>
.v-toolbar {
  transition: 0.6s;
}
active-class {
  color: red;
}

.v-btn {
  z-index: 999;
}
</style>
