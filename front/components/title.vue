<template>
      <p class="display-2 text-center font-weight-bold mt-12 mb-12"> {{this.value}}  <span id="explore"></span></p>
</template>
<script>
export default {
   props: ["value"],
}
</script>
<style lang="scss" scoped>

#explore{
    background-color: #5C6BC0;
    width: 80px;
    height: 8px;
    margin: 0 auto;
    display: block;
    margin-top: 10px;
}
</style>
