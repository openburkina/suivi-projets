export const state = () => ({
  baillleurs: [],
  projects: [],
  errors: [],
  name: "",
  secteurs: [],
  montantSecteurParBailleur: [],
})

export const mutations = {
  SET_MONTANT_SECTEUR_PAR_BAILLEUR(state, payload) {
    state.montantSecteurParBailleur = payload
  },
  SET_SECTEURS_DATA(state, payload) {
    state.secteurs = payload
  },
  SET_NAME(state, payload) {
    state.name = payload
  },
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
  getMontantParSecteurParRegion({ commit }, payload) {
    return new Promise((resolve, reject) => {
      this.$axios
        .get(`/projects-budget-sector-year-org`)
        .then((response) => {
          let data = response.data.filter((d) => d.organisation == payload)
          const jsonHelper = require('./../utils/jsonHelper');
          const amountsSectors = jsonHelper.amountsSectors(data);

          const final = {
            options: {
              chart: {
                id: 'line-chart-montant-secteur-par-bailleur',
              },
              xaxis: {
                categories: amountsSectors.categories,
              }
            },
            series: amountsSectors.series,
          }
          commit('SET_MONTANT_SECTEUR_PAR_BAILLEUR', final)
          resolve()
        })
        .catch((error) => {
          if (error.response) {
            console.log('Error in Patient Data process...!')
          }
          commit('SET_ERRORS', 'Error in Patient Data process...!')
        })
    })
  },
  getSecteurs({ commit }, payload) {
    return new Promise((resolve, reject) => {
      this.$axios
        .get(`/sector-name`)
        .then((response) => {
          commit('SET_SECTEURS_DATA', response.data)
          resolve()
        })
        .catch((error) => {
          if (error.response) {
            console.log('Error in Patient Data process...!')
          }
          commit('SET_ERRORS', 'Error in Patient Data process...!')
        })
    })
  },
  getName({ commit }, payload) {
    let search = payload ? payload : ''
    return new Promise((resolve, reject) => {
      this.$axios
        .get(`/organisation-list/${payload}`)
        .then((response) => {
          commit('SET_NAME', response.data.org_name)
          resolve()
        })
        .catch((error) => {
          if (error.response) {
            console.log('Error in Patient Data process...!')
          }
          commit('SET_ERRORS', 'Error in Patient Data process...!')
        })
    })
  },
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
