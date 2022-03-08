<template>
  <div>
    <p class="display-2 text-center font-weight-bold mb-5 mt-3">
      <span class="dark--text">{{ this.value }} </span> 
      <span id="explore" class="primary"></span>
    </p>
  </div>
</template>
<script>
export default {
  props: ['value'],
}
</script>
<style lang="scss" scoped>
#explore {
  width: 80px;
  height: 8px;
  margin: 0 auto;
  display: block;
  margin-top: 10px;
}
</style>
