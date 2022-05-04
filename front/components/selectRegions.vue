<template>
  <div>
    <ListeMenu :menus="regions" />
  </div>
</template>
<script>
import { mapGetters, mapState, mapActions } from 'vuex'
export default {
  async asyncData({ store }) {
    await Promise.all([
      store.dispatch('region/getRegionsData'),
    ])
    return
  },

  data() {
    return {}
  },

  computed: {
    ...mapState('region', {
      regions: (state) => state.regions,
      errors: (state) => state.errors,
    }),
  },
  //   async asyncData({ $axios }) {
  //     let { data } = await $axios.get('/menu')
  //     return { regions: data }
  //   },
  //   methods: {
  //     async getIncidents() {
  //       let res = await this.$store.dispatch('getIncidents')
  //       this.regions = res.data
  //     },
  //   },
}
</script>