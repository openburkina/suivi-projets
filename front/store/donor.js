export const state = ()=> ({
    donors: [],
    data: [],
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
        this.$axios.get('/fin_split_up/').then((response)=> {
          console.log(response.data)
          commit('SET_DONOR_DATA', response.data)
          resolve()
          // console.log(response.data)
        })
      })
    },
  }
  