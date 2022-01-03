export const state = ()=> ({
  projects3: [],
  data: [],
  errors: []
})

export const mutations = {
  SET_SECTAGREG_DATA(state, payload){
    state.projects3 = payload
  },
}

export const actions = {
  getSect_AggregateData({commit}, payload){
    return new Promise((resolve, reject)=> {
      this.$axios.get('/sector_aggregate/').then((response)=> {
        console.log(response.data)
        commit('SET_SECTAGREG_DATA', response.data)
        resolve()
        // console.log(response.data)
      })
    })
  },
}
