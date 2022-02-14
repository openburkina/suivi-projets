<template>
  <div>
    <TabsDetailProjet/>
  </div>
</template>
<script>

import {mapState} from 'vuex'

export default {

  async asyncData({store, params}){
    await Promise.all([
      store.dispatch('project/getProjectInfo', params.id),
      store.dispatch('project/getProjectActivities', params.id),
      store.dispatch('project/getProjectAmounts', params.id),
      store.dispatch('project/getProjectIndicators', params.id)
    ])
      return
  },
  
  data() {
    return {
      search: '',
      id_projet: this.$route.params.id,
      tab: null,
     
    }
  },


  methods: {
    getTitle(message) {
      return `${message} sur le projet : ${this.id_projet}`
    },
  },
}
</script>