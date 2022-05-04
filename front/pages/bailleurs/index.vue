<template>
  <div>
    <TabBailleurContent/>
  </div>
</template>
<script>
export default {
  async asyncData({ store }) {
    await Promise.all([
      store.dispatch('bailleur/getBailleursData'),
      store.dispatch('bailleur/getBailleursProjectData'),
      store.dispatch('bailleur/getBailleursSecteurtData'),
      store.dispatch('bailleur/getBailleursRegiontData'),
    ])
    return
  },
}
</script>