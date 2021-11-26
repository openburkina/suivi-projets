<template>
  <v-container style="margin-top: -90px">
    <v-row>
      <v-col cols="4"> </v-col>
      <v-col cols="4" class="text-center">
        <div class="info--text font-weight-bold display-2 mx-auto">Project detail</div>
        <hr style="height: 5px; background: #2196f3; border-color: #2196f3; border-radius: 10px;" />
      </v-col>
      <v-col cols="4"> </v-col>
    </v-row>

    <v-row>
        <ProjectDetail/>
    </v-row>
  </v-container>
</template>

<script>
export default {
    head() {
    return {
      title: 'Detail\'s project',
    }
  },
}
</script>