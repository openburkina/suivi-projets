<template>
  <div>
    <v-list>
      <v-list-item>
        <v-list-item-content>
          <img :src="require('~/assets/img/pnud.png')" height="100" />
        </v-list-item-content>
      </v-list-item>
    </v-list>

    <v-divider />

    <v-list nav dense>
      <v-list-item-group active-class="deep-purple--text text--accent-4">
        <v-list-item to="/">
          <v-list-item-icon>
            <v-icon>mdi-home</v-icon>
          </v-list-item-icon>
          <v-list-item-title>Accueil</v-list-item-title>
        </v-list-item>
        <v-list-item to="/projets">
          <v-list-item-icon>
            <v-icon>mdi-office-building</v-icon>
          </v-list-item-icon>
          <v-list-item-title>Projets</v-list-item-title>
        </v-list-item>

        <v-list-item to="/bailleurs">
          <v-list-item-icon>
            <v-icon>mdi-billiards</v-icon>
          </v-list-item-icon>
          <v-list-item-title>Bailleurs</v-list-item-title>
        </v-list-item>

        <v-list-item to="/regions">
          <v-list-item-icon>
            <v-icon>mdi-google-maps</v-icon>
          </v-list-item-icon>
          <v-list-item-title>R&eacute;gions</v-list-item-title>
        </v-list-item>
      </v-list-item-group>
    </v-list>
  </div>
</template>
