export const state = () => ({
  montants: [],
  errors: [],
})

export const mutations = {
  SET_MONTANTS_DATA(state, payload) {
    state.montants = payload
  },
  SET_ERRORS(state, payload) {
    state.errors = payload
  },
}

export const actions = {
  getMontantSecteursDataForChart({ commit }, payload) {
    return new Promise((resolve, reject) => {
      this.$axios
        .get(`/projects-budget-sector-year`)
        .then((response) => {
          const data = response.data
          let sectorList = [...new Set(data.map((x) => x.sector))]
          sectorList = sectorList.filter((x) => x != null && x != undefined)
          let amountsSectors = []
          sectorList.map((sector) => {
            let val = { x: sector, y: 0 }
            data.map((d) => {
              if (d.sector == sector) val.y += parseInt(d.sum)
            })
            // val.y = new Intl.NumberFormat('en-US', {style: 'currency', currency: 'USD'}).format(val.y)
            amountsSectors.push(val)
          })
          const final = {
            options: {
              chart: {
                id: 'line-chart-montant-secteur',
              },
              xaxis: {
                categories: sectorList,
              }
            },
            series: [{data:amountsSectors}],
          }
          commit('SET_MONTANTS_DATA', final)
          resolve()
        })
        .catch((error) => {
          if (error.response) {
            console.log('Error in Patient Data process...!')
          }
          commit('SET_ERRORS', 'Error in Patient Data process...!')
        })
    })
  },

  getMontantSecteursData({ commit }, payload) {
    return new Promise((resolve, reject) => {
      this.$axios
        .get(`/projects-budget-sector`)
        .then((response) => {
          commit('SET_MONTANTS_DATA', response.data)
          resolve()
        })
        .catch((error) => {
          if (error.response) {
            console.log('Error in Patient Data process...!')
          }
          commit('SET_ERRORS', 'Error in Patient Data process...!')
        })
    })
  },
}
