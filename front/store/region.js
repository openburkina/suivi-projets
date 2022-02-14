export const state = () => ({
  regions: [],
  projects: [],
  errors: [],
})

export const mutations = {
  SET_REGION_DATA(state, payload) {
    state.regions = payload
  },
  SET_PROJECTS_DATA(state, payload) {
    state.projects = payload
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
      }).catch((error)=> {
        if(error.response){
          console.log("Error in Patient Data process...!")
        }
        commit('SET_ERRORS', "Error in Patient Data process...!")
      })
    })
  },
  getProjectsData({commit}, payload){
    return new Promise((resolve, reject)=> {
      this.$axios.get(`/region-project-list/?q=${payload}`).then((response)=> {
        commit('SET_PROJECTS_DATA', response.data)
        resolve()
        console.log(`/region-project-list/?q=${payload}`)
      }).catch((error)=> {
        if(error.response){
          console.log("Error in Patient Data process...!")
        }
        commit('SET_ERRORS', "Error in Patient Data process...!")
      })
    })
  },
}
