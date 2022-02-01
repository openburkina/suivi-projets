export default {
  methods: {
    getColor1(statut) {
      if (statut < 1) return '#00E396'
      else return '#008FFB'
    },
    getValue1(statut) {
      if (statut < 1) return 'mdi-close'
      else return 'mdi-check'
    },
  },
}
