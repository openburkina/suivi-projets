import axios from 'axios'
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
        this.$axios.get('/projets1').then((response)=> {
          commit('SET_PROJECT_DATA', response.data)
          resolve()
          console.log(response.data)
        })
      })
    },
  
    storeProjectsData({dispatch, commit}, payload){
      return new Promise((resolve, reject)=> {
         console.log(payload)
        this.$axios.post('/projects', payload).then(()=> {
          dispatch('getProjectsData')
          resolve()
          console.log(response.data)
        }).catch((error)=> {
          // console.log(error.response.data)
          commit('SET_ERRORS', error.response)
        })
      })
    },
  
    getProjectData({commit}, payload){
      return new Promise((resolve, reject)=> {
        this.$axios.get(`/projects/${payload}`).then((response)=> {
          commit('SET_DATA', response.data)
          resolve()
          console.log(response.data)
        })
      })
    },
  
    updateProjectData({dispatch, commit}, payload){
      return new Promise((resolve, reject)=> {
        console.log(payload)
        this.$axios.put(`/projects/${payload.id}`, payload).then(()=> {
          dispatch('getProjectsData')
          resolve()
          // console.log(response.data)
        }).catch((error)=> {
          // console.log(error.response.data)
          commit('SET_ERRORS', error.response.data)
        })
      })
    },
  
    destroyProjectData({dispatch, commit}, payload){
      return new Promise((resolve, reject)=> {
        this.$axios.delete(`/projects/${payload}`).then(()=> {
          dispatch('getProjectsData')
          resolve()
          console.log(response.data)
        }).catch((error)=> {
          console.log(error.response.data)
          commit('SET_ERRORS', error.response.data)
        })
      })
    }
  }
  
  let instance = axios.create({
    headers: {
      get: {        // can be common or any other method
        header1: 'value1'
      }
    }
  })
  instance.defaults.headers.get['header']=''