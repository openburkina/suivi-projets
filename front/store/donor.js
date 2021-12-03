export const state = ()=> ({
    donors: [],
    data: [],
    formEdit:{

    },
    errors: []
  })
  
  export const mutations = {
    SET_DONOR_DATA(state, payload){
      state.donors = payload
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
    getDonorsData({commit}, payload){
      return new Promise((resolve, reject)=> {
        this.$axios.get('/v1/donor/budget_sources?year=2021').then((response)=> {
          console.log(response.data.data)
        //  this.$axios.get('/donors').then((response)=> {
          commit('SET_DONOR_DATA', response.data.data)
          resolve()
          // console.log(response.data)
        })
      })
    },
  
    storeDonorsData({dispatch, commit}, payload){
      return new Promise((resolve, reject)=> {
        // console.log(payload)
        this.$axios.post('/donors', payload).then((response)=> {
          dispatch('getDonorsData')
          resolve()
           console.log(response.data)
        }).catch((error)=> {
          // console.log(error.response.data)
          commit('SET_ERRORS', error.response)
        })
      })
    },
  
    getDonorData({commit}, payload){
      return new Promise((resolve, reject)=> {
        this.$axios.get(`/donors/${payload}`).then((response)=> {
          commit('SET_DATA', response.data)
          resolve()
          console.log(response.data)
        })
      })
    },
  
    updateDonorData({dispatch, commit}, payload){
      return new Promise((resolve, reject)=> {
         console.log(payload)
         this.$axios.put(`/donors/${payload.id}`, payload).then(()=> {
          dispatch('getDonorsData')
          resolve()
          // console.log(response.data)
        }).catch((error)=> {
          // console.log(error.response.data)
          commit('SET_ERRORS', error.response.data)
        })
      })
    },
  
    destroyDonorData({dispatch, commit}, payload){
      return new Promise((resolve, reject)=> {
        this.$axios.delete(`/donors/${payload}`).then(()=> {
          dispatch('getDonorsData')
          resolve()
          console.log(response.data)
        }).catch((error)=> {
          console.log(error.response.data)
          commit('SET_ERRORS', error.response.data)
        })
      })
    },

    formEditData({commit}, data){
      return new Promise((resolve, reject)=> {
           console.log(data)
          commit('SET_DONOR_EDIT_DATA', data)
          resolve()
      })
    },
  }
  