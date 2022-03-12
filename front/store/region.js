export const state = () => ({
  regions: [],
  projects: [],
  lats: [],
  errors: [],
})

export const mutations = {
  SET_REGION_DATA(state, payload) {
    state.regions = payload
  },
  SET_PROJECTS_DATA(state, payload) {
    state.projects = payload
  },
/* 
  SET_REGION_LAT(state, payload) {
    state.projects = payload
  },
 */

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
        console.log(response.data)
      } 
    
      ).catch((error)=> {
        if(error.response){
          console.log("Error in Patient Data process...!")
        }
        commit('SET_ERRORS', "Error in Patient Data process...!")
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
