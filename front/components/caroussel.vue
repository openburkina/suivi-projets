<template>
  <v-carousel cycle hide-delimiters show-arrows-on-hover height="500">
    <v-carousel-item
      v-for="(item, i) in items"
      :key="i"
      :src="item.src"
    ></v-carousel-item>
  </v-carousel>
</template>

<script>
export default {
  data() {
    return {
      items: [
        {
          src: require('~/assets/img/image3.jpg'),
        },
        {
          src: require('~/assets/img/image1.jpg'),
        },
        {
          src: require('~/assets/img/image2.jpg'),
        },
      ],
    }
  },
}
</script>
