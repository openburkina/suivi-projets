<template>
  <v-app-bar color="primary" dark >
    <img :src="require('../../assets/images/logo.png')" style="margin-right: 10%; width:60px"/>
    <router-link to="bailleur"
      ><v-btn style="margin: 3px" text 
        >Bailleurs</v-btn
      ></router-link
    >
    <router-link to="projectList"
      ><v-btn style="margin: 3px" text plain class="activeLien"
        >Projets</v-btn
      ></router-link
    >
  </v-app-bar>
</template>
<script>
export default {
  props:{
    activeLink: String
  },
  computed :{
      isActive : function(link){
        if (this.activeLink != link)
          return "plain";
      }
   }
}
</script>
<style lang="css">
  .v-btn .v-btn::before {
    border-color: grey !important;
  }
</style>