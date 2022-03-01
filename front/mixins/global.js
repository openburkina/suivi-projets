export default {
  
  methods: {
    // getColor(statut) {
    //   if (statut < 1) return '#00E396'
    //   else return '#008FFB'
    // },
    // getValue(statut) {
    //   if (statut < 1) return 'mdi-close'
    //   else return 'mdi-check'
    // },
    // createEditLink(item) {
    //   return this.$router.push({ path: '/projets/detail/' + item.id })
    // },

    // filtering
    getNameBailleur(bailleurs, idBailleur){
      bailleurs.map((bailleur)=>{
        if(bailleur.ref_id == idBailleur){
          return bailleur.org_name;
        }
        return "Not found";
      });
    },

    getNameRegion(regions, idregion){
      regions.map((region)=>{
        if(region.region_code == idregion){
          return region.name;
        }
        return "Not found";
      });
    }
  },
}
