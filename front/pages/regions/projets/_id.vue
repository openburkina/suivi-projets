<template>
  <div>
    <TabRegionContent  />
  </div>
</template>

<script>
export default {
  async asyncData({ store, params }) {
    await Promise.all([
      store.dispatch('region/getProjectsData', params.id),
      store.dispatch('region/getMontantParSecteurParRegion', params.id),
      store.dispatch('region/getMontantParBailleurParRegion', params.id),
      store.dispatch('region/getMontantParStatusParRegion', params.id),
      store.dispatch('region/getSecteurs'),
      store.dispatch('region/getBailleurs'),
    ])
    return
  },
}
</script>