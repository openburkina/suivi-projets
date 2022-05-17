<template>
  <div>
    <TabsDetailProjet/>
  </div>
</template>
<script>
import axios from 'axios'
export default {
  // generate: {
  //   routes() {
  //     return axios.get('https://djangosp.herokuapp.com/api/project-list').then(res => {
  //       return res.data.map(item => {
  //         return '/projets/detail/' + item.project_id
  //       })
  //     })
  //   }
  // },
  async asyncData({store, params}){
    await Promise.all([
      store.dispatch('project/getProjectInfo', params.id),
      store.dispatch('project/getProjectActivities', params.id),
      store.dispatch('project/getProjectAmounts', params.id),
      store.dispatch('project/getProjectIndicators', params.id)
    ])
      return
  },
}
</script>