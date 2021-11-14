<template>
  <v-footer dark padless>
    <v-row justify="center" no-gutters>
      <v-btn
        v-for="link in links"
        :key="link"
        color="white"
        text
        rounded
        class="my-2"
      >
        {{ link }}
      </v-btn>
      <v-col class="dark lighten-2 py-4 text-center white--text" cols="12">
        <small
          ><v-icon slot="icon" color="white" size="20">
            mdi-copyright </v-icon
          > - Copyright {{ new Date().getFullYear() }}. All rigth reserved. 
        </small>
      </v-col>
    </v-row>
  </v-footer>
</template>
<script>
export default {
  data: () => ({
    links: [
        'About us', 
        'Sustainable Development ', 
        'Goals', 
        'Partners', 
        'Report fraud, abuse, misconduct', 
        'Submit social or environmental complaint', 
        'Scam alertTerms of use', 
        'Download', 
    ],
        
  }),
}
</script>