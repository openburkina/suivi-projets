export const state = ()=> ({
  projects2: [],
  data: [],
  formEdit:{

  },
  errors: []
})

export const mutations = {
  PROJ_SECTAGREG_DATA(state, payload){
    state.projects2 = payload
  },
  SET_DONOR_EDIT_DATA(state, payload){
    state.formEdit = payload
    console.log(state.formEdit);
  },
  SET_DATA(state, payload){
    state.data = payload
  },
  SET_ERRORS(state, payload){
    state.errors = payload
  }
}
export const actions = {
  getProj_AggregateData({commit}, payload){
    return new Promise((resolve, reject)=> {
      this.$axios.get('/project_aggregate/').then((response)=> {
        console.log(response.data)
        commit('PROJ_SECTAGREG_DATA', response.data)
        resolve()
        console.log(response.data)
      })
    })
  },

  
}
