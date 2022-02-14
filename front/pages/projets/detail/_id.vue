<template>
  <div>
    <TabsDetailProjet/>
  </div>
</template>
<script>
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
}
</script>