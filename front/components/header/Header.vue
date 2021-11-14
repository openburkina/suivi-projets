<template>
    <v-app-bar
        color="primary accent-4"
        class="mb-3"
        dark
      >
        <v-app-bar-nav-icon></v-app-bar-nav-icon>
        <v-toolbar-title></v-toolbar-title>
        <v-spacer></v-spacer>
        <v-btn depressed color="primary" style="margin: 3px;" class="elevation-1">Home</v-btn>
        <v-btn depressed color="primary" style="margin: 3px;" class="elevation-1">Projects</v-btn>
        <v-btn depressed color="primary" style="margin: 3px;" class="elevation-1">Donors</v-btn>
        <v-btn depressed color="primary" style="margin: 3px;" class="elevation-1">Sustainable development goals</v-btn>
        <v-btn depressed color="primary" style="margin: 3px;" class="elevation-1">OUR APPROACHES</v-btn>
        <v-btn depressed color="primary" style="margin: 3px;" class="elevation-1">MORE</v-btn>
        <v-btn icon>
          <v-icon>mdi-magnify</v-icon>
        </v-btn>
  
        <v-menu
          left
          bottom
        >
          <template v-slot:activator="{ on, attrs }">
            <v-btn
              icon
              v-bind="attrs"
              v-on="on"
            >
              <v-icon>mdi-dots-vertical</v-icon>
            </v-btn>
          </template>
  
          <v-list>
            <v-list-item
              v-for="n in 5"
              :key="n"
              @click="() => {}"
            >
              <v-list-item-title>Option {{ n }}</v-list-item-title>
            </v-list-item>
          </v-list>
        </v-menu>
      </v-app-bar>
</template>
<script>
export default {
    data: () => ({
    items: [
      { title: 'Click Me' },
      { title: 'Click Me' },
      { title: 'Click Me' },
      { title: 'Click Me 2' },
    ],
  }),
}
</script>