<template>
<div>
        <p class="white--text font-weight-bold mx-auto display-1 mt-15">
        Portail de transparence du PNUD
        </p>
        <p class="white--text mx-auto">
            Au PNUD, nous nous engageons à éradiquer la pauvreté, à lutter contre le changement climatique et à réduire
        </p>
        <p class="white--text mx-auto">
           inégalités et exclusions dans le monde. Découvrez comment, avec l'aide de nos partenaires, nous travaillons
             jour après jour pour en faire une réalité.
        </p>
    <v-text-field
        placeholder="Search using Project,Donors, Recipients or Keyword"
        solo
        clearable
        append-icon="mdi-magnify"
        style="width: 500px;"
        class="mx-auto mt-5"
        
    > 
    </v-text-field>
     <div class="mx-auto py-5 mb-5">
        <v-btn icon size="60"><v-icon size="60" color="white">mdi-menu-left</v-icon></v-btn>
        <span class="white--text font-weight-bold">2021</span>
        
        <v-btn icon size="60"><v-icon size="60" color="white">mdi-menu-right</v-icon></v-btn>
    </div>
       
    <ButtonGroup />
    <ResponsiveButtonGroup />
    
</div>
</template>

<style scoped>
.v-btn i:hover{
  transform: scale(2.15);
  transition: width 1s, height 1s, transform 1s;

}
</style>