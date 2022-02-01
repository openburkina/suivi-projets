<template>
  <div>
    <hr />
    <h1>Liste Region</h1>
    <div
      v-for="menu in menus"
      :key="menu.region_code"
    >
    <p>{{menu.name}} </p>
    <span class="mx-1 accent--text">{{menu.region_code}} </span>
    </div>
  </div>
</template>
<script>
export default {
  props: {
    menus: Array,
  },
}
</script>
