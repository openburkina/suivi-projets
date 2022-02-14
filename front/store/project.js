export const state = ()=> ({
    projects: [],
    project: '',
    activities: [],
    amounts: [],
    indicators: [],
    errors: []
  })
  
  export const mutations = {
    SET_PROJECT_DATA(state, payload){
      state.projects = payload
    },
    SET_DATA(state, payload){
      state.project = payload
    },
    SET_ACTIVITIES(state, payload){
      state.activities = payload
    },
    SET_AMOUNTS(state, payload){
      state.amounts = payload
    },
    SET_INDICATORS(state, payload){
      state.indicators = payload
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
           //console.log(response.data)
        })
      })
    }, 
    
    getProjectInfo({commit}, id){
      return new Promise((resolve, reject)=> {
        this.$axios.get(`/project-info/${id}`).then((response)=> {
          commit('SET_DATA', response.data)
          resolve()
          //  console.log(response.data)
        }).catch((error)=> {
          if(error.response){
            console.log("Error in Patient Data process...!")
          }
          commit('SET_ERRORS', "Error in Patient Data process...!")
        })
      })
    },

    getProjectActivities({commit}, payload){
      return new Promise((resolve, reject)=> {
        this.$axios.get(`/project-act/?q=${payload}`).then((response)=> {
          commit('SET_ACTIVITIES', response.data)
          resolve()
          // console.log(response.data)
        }).catch((error)=> {
          if(error.response){
            console.log("Error in Patient Data process...!")
          }
          commit('SET_ERRORS', "Error in Patient Data process...!")
        })
      })
    },

    getProjectAmounts({commit}, payload){
      return new Promise((resolve, reject)=> {
        this.$axios.get(`/project-dec/?q=${payload}`).then((response)=> {
          commit('SET_AMOUNTS', response.data)
          resolve()
          // console.log(response.data)
        }).catch((error)=> {
          if(error.response){
            console.log("Error in Patient Data process...!")
          }
          commit('SET_ERRORS', "Error in Patient Data process...!")
        })
      })
    },

    getProjectIndicators({commit}, payload){
      return new Promise((resolve, reject)=> {
        this.$axios.get(`/project-ind/?q=${payload}`).then((response)=> {
          commit('SET_INDICATORS', response.data)
          resolve()
          // console.log(response.data)
        }).catch((error)=> {
          if(error.response){
            console.log("Error in Patient Data process...!")
          }
          commit('SET_ERRORS', "Error in Patient Data process...!")
        })
      })
    },
  
  }