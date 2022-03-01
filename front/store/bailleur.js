export const state = () => ({
  baillleurs: [],
  projects: [],
  errors: [],
})

export const mutations = {
  SET_REGION_DATA(state, payload) {
    state.baillleurs = payload
  },
  SET_PROJECTS_DATA(state, payload) {
    state.projects = payload
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
      this.$axios.get(`/org-project-list/?q=${payload}`).then((response)=> {
        commit('SET_PROJECTS_DATA', response.data)
        resolve()
        console.log(`/org-project-list/?q=${payload}`)
      }).catch((error)=> {
        if(error.response){
          console.log("Error in Patient Data process...!")
        }
        commit('SET_ERRORS', "Error in Patient Data process...!")
      })
    })
  },
}
