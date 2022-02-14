export default {
  
  methods: {
    getColor(statut) {
      if (statut < 1) return '#00E396'
      else return '#008FFB'
    },
    getValue(statut) {
      if (statut < 1) return 'mdi-close'
      else return 'mdi-check'
    },
    createEditLink(item) {
      return this.$router.push({ path: '/projets/detail/' + item.id })
    },
  },
}
