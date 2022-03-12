export const state = () => ({
  bailleurs: [],
  mount: [],
  secteurs:[],
  bailleurs_count: [],
  bailleurs_label: [],
  errors: [],

  series_secteurs: [
    {
      name: '',
      data: [],
    },
  ],

  series_regions: [
    {
      name: '',
      data: [],
    },
  ]
})

export const mutations = {

  SET_BAILLLEUR_DATA(state, payload) {
    state.bailleurs = payload
  },

  SET_BAILLLEUR_PROJECT_DATA(state, payload) {
    state.bailleurs = payload
  },

  SET_BAILLLEUR_PROJECT_STATUS(state, payload) {
     // console.log(payload)
    for (let i = 0; i < payload.length; i++) {
       state.bailleurs_label.push(payload[i].organisation);
       
    }
    // console.log("The List: " + state.bailleurs_label);
    for (let i = 0; i < payload.length; i++) {
      state.bailleurs_count.push(parseInt(payload[i].activity_status));
      //console.log("The List: " + state.bailleurs_count);
    }
  },

  SET_BAILLLEUR_SECTEUR_DATA(state, payload) {
    for (let i = 0; i < payload.length; i++) {
      state.series_secteurs[0].data[i] = payload[i].sum;
     // console.log("The List: " + state.bailleurs_count);
    }
  },

  SET_BAILLLEUR_REGION_DATA(state, payload) {
    for (let i = 0; i < payload.length; i++) {
      state.series_regions[0].data[i] = payload[i].sum;
      // console.log("The List: " + state.bailleurs_count);
    }
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
        commit('SET_BAILLLEUR_DATA', response.data)
        resolve()
      //console.log(response.data)
      })
    })
  },

  getBailleursData({ commit }, payload) {
    let search = payload ? payload : ''
    return new Promise((resolve, reject) => {
      this.$axios.get('/organisation-list').then((response) => {
        commit('SET_BAILLLEUR_DATA', response.data)
        resolve()
      //console.log(response.data)
      })
    })
  },

  getBailleursProjectData({ commit }, payload) {
    let search = payload ? payload : ''
    return new Promise((resolve, reject) => {
      this.$axios.get('/projects-status-year-org').then((response) => {
        commit('SET_BAILLLEUR_PROJECT_STATUS', response.data)
        resolve()
       // console.log(response.data)
      })
    })
  },

  getBailleursSecteurtData({ commit }, payload) {
    let search = payload ? payload : ''
    return new Promise((resolve, reject) => {
      this.$axios.get('/projects-budget-sector-year').then((response) => {
        commit('SET_BAILLLEUR_SECTEUR_DATA', response.data)
        resolve()
        // console.log(response.data)
      })
    })
  },
 
  getBailleursRegiontData({ commit }, payload) {
    let search = payload ? payload : ''
    return new Promise((resolve, reject) => {
      this.$axios.get('/projects-budget-region-year').then((response) => {
        commit('SET_BAILLLEUR_REGION_DATA', response.data)
        resolve()
        // console.log(response.data)
      })
    })
  },
   

}
