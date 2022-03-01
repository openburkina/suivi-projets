<template>
  <div>
    <TabBailleurContent  />
  </div>
</template>

<script>
export default {
  async asyncData({ store, params }) {
    console.log('bailleur/getProjectsData/'+ params.id);
    await Promise.all([
      store.dispatch('bailleur/getProjectsData', params.id),
    ])
    return
  },
}
</script>