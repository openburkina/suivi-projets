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
    ])
    return
  },
}
</script>