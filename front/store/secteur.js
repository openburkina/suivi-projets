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
        .get(`/projects-budget-sector`)
        .then((response) => {
          const data = response.data;
          // const jsonHelper = require('./../utils/jsonHelper');
          // const amountsSectors = jsonHelper.amountsSectors(data);

          // const final = {
          //   options: {
          //     chart: {
          //       id: 'line-chart-montant-secteur',
          //     },
          //     xaxis: {
          //       categories: amountsSectors.categories,
          //     }
          //   },
          //   series: amountsSectors.series,
          // }
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
