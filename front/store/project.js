export const state = ()=> ({
    projects: [],
    data: [],
    errors: []
  })
  
  export const mutations = {
    SET_PROJECT_DATA(state, payload){
      state.projects = payload
    },
    SET_DATA(state, payload){
      state.data = payload
    },
    SET_ERRORS(state, payload){
      state.errors = payload
    }
  }
  export const actions = {
    getProjectsData({commit}, payload){
      let search = payload ? payload : ''
      return new Promise((resolve, reject)=> {
        this.$axios.get('/project-list').then((response)=> {
          commit('SET_PROJECT_DATA', response.data)
          resolve()
           console.log(response.data)
        })
      })
    },   
  }