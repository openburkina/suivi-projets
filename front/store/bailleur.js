export const state = () => ({
  bailleurs: [],
  errors: [],
})

export const mutations = {
  SET_BAILLLEUR_DATA(state, payload) {
    state.bailleurs = payload
  },
  SET_ERRORS(state, payload) {
    state.errors = payload
  },
}
export const actions = {
  getBailleursData({ commit }, payload) {
    let search = payload ? payload : ''
    return new Promise((resolve, reject) => {
      this.$axios.get('/organisation-list').then((response) => {
        commit('SET_BAILLLEUR_DATA', response.data)
        resolve()
      //  console.log(response.data)
      })
    })
  },
}
