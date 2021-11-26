<template>
  <v-card flat tile class="indigo lighten-1 white--text text-center">
    <v-card-text>
      <v-btn v-for="icon in icons" :key="icon" class="mx-4 white--text" icon>
        <v-icon size="24px">
          {{ icon }}
        </v-icon>
      </v-btn>
    </v-card-text>
    <v-card-text>
      <v-btn
        v-for="link in links"
        :key="link"
        class="indigo lighten-1 white--text text-center"
        elevation="0"
        rounded
      >
        {{ link }}
      </v-btn>
    </v-card-text>

    <v-divider></v-divider>

    <v-card-text class="white--text">
      <strong>Data last updated on, 3 November 2021</strong>
    </v-card-text>
  </v-card>
</template>
<script>
export default {
  data: () => ({
    icons: ['mdi-facebook', 'mdi-twitter', 'mdi-linkedin', 'mdi-instagram'],
    links: [
      'About us',
      'Sustainable Development Goals',
      'Partners',
      'Report fraud, abuse, misconduct',
      'Submit social or environmental complaint',
      'Scam alert',
      'Terms of use',
    ],
  }),
}
</script>
