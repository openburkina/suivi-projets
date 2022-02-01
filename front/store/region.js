export const state = () => ({
  regions: [],
  errors: [],
})

export const mutations = {
  SET_REGION_DATA(state, payload) {
    state.regions = payload
  },
  SET_ERRORS(state, payload) {
    state.errors = payload
  },
}
export const actions = {
  getRegionsData({ commit }, payload) {
    let search = payload ? payload : ''
    return new Promise((resolve, reject) => {
      this.$axios.get('/region-list').then((response) => {
        commit('SET_REGION_DATA', response.data)
        resolve()
        console.log(response.data)
      })
    })
  },
}
