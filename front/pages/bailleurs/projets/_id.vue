<template>
  <div>
    <TabBailleurContent />
  </div>
</template>

<script>
export default {
  async asyncData({ store, params }) {
    await Promise.all([
      store.dispatch('bailleur/getProjectsData', params.id),
      store.dispatch('bailleur/getName', params.id),
      store.dispatch('bailleur/getSecteurs'),
      store.dispatch('bailleur/getMontantParSecteurParRegion', params.id),
    ])
    return
  },
}
</script>
