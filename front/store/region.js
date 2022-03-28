export const state = () => ({
  regions: [],
  projects: [],
  project_status: [],
  lats: [],
  errors: [],
  count_end : 0,
  count_going : 0
})

export const mutations = {
  SET_REGION_DATA(state, payload) {
    state.regions = payload
  },
  SET_PROJECTS_DATA(state, payload) {
    state.projects = payload
  },
 
  SET_REGION_PROJECT_STATUS(state, payload) {
    
    for (let i = 0; i < payload.length; i++) {

      if(payload[i].activity_status == 1){
        // console.log('Console: ' + parseInt(payload[i].count))
       state.count_end += parseInt(payload[i].count) 
      } else if(payload[i].activity_status == 0){
        // console.log('Console: ' + parseInt(payload[i].count))
       state.count_going += parseInt(payload[i].count) 
      }
    }
    state.project_status[0] = state.count_end
    state.project_status[1] = state.count_going
    console.log(state.project_status)
    
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
      //  console.log(response.data)
      })
    })
  },

  getProjectsData({commit}, payload){
    return new Promise((resolve, reject)=> {
      this.$axios.get(`/region-project-list/?q=${payload}`).then((response)=> {
        commit('SET_PROJECTS_DATA', response.data)
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


  getRegionsLats({commit}, id){
    return new Promise((resolve, reject)=> {
      this.$axios.get(`/region-detail/${id}`).then((response)=> {
       // commit('SET_PROJECTS_DATA', response.data)
        resolve()
        // console.log(response.data)
      } 
    
      ).catch((error)=> {
        if(error.response){
          console.log("Error in Patient Data process...!")
        }
        commit('SET_ERRORS', "Error in Patient Data process...!")
      })
    })
  },


  getRegionsProjectStatus({ commit }, payload) {
    return new Promise((resolve, reject) => {
      this.$axios.get('/projects-status-year-region').then((response) => {
        commit('SET_REGION_PROJECT_STATUS', response.data)
        resolve()
       // console.log(response.data)
      })
    })
  },

/* 
for (let i = 0; i < state.regions.length; i++) {
      console.log("length: " + state.regions.length)
     }
  getRegionsLat({ commit }, payload) {
    return new Promise((resolve) => {
      this.$axios.get('/region-list').then((response) => {
        commit('SET_REGION_LAT', response.data)
        resolve()
      //  console.log(response.data)
      })
    })
  },
   */
}
