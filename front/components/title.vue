<template>
  <div>
    <p class="display-1 text-center font-weight-bold mb-5 mt-3">
      <span>{{ this.value }} </span> 
      <span id="explore"></span>
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
  height: 6px;
  margin: 0 auto;
  display: block;
  margin-top: 10px;
  background: #416e80;
}
span{
  color: #416e80;
}
</style>
