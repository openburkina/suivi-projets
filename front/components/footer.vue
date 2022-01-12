<template>
  <v-footer color="indigo lighten-1" padless>
    <v-row justify="center" no-gutters>
      
      <v-btn
        v-for="link in links"
        :key="link"
        color="white"
        text
        rounded
        class="my-1"
      >
        {{ link }}
      </v-btn>
      <v-col class="indigo lighten-1 text-center my-1" cols="12">
        <v-btn v-for="icon in icons" :key="icon" class="mx-5" icon color="white">
          <v-icon size="24px">
            {{ icon }}
          </v-icon>
        </v-btn>
      </v-col>
      <v-col class="indigo lighten-2 py-4 text-center white--text" cols="12">
        {{ new Date().getFullYear() }} — <strong>Suivi de projets</strong>
      </v-col>
    </v-row>
  </v-footer>
</template>
<script>
export default {
  data: () => ({
    icons: ['mdi-facebook', 'mdi-twitter'],
    links: ['A propos', 'Partenaires', "Termes d'utilisation", 'Télécharger'],
  }),
}
</script>
