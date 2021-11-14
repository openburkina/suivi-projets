<template>
    <v-app id="inspire" style="height:60px">
    <v-combobox
      v-model="chips"
      :items="items"
      chips
      clearable
      label="Filtre par projet"
      multiple
      solo
    >
      <template v-slot:selection="{ attrs, item, select, selected }">
        <v-chip
          v-bind="attrs"
          :input-value="selected"
          close
          @click="select"
          @click:close="remove(item)"
        >
          <strong>{{ item }}</strong>&nbsp;
        </v-chip>
      </template>
    </v-combobox>
  </v-app>
</template>
<script>
export default {
   data () {
    return {
      chips: [],
      items: ['Terminer', 'En cours'],
    }
  },

  methods: {
    remove (item) {
      this.chips.splice(this.chips.indexOf(item), 1)
      this.chips = [...this.chips]
    },
  }
}
</script>