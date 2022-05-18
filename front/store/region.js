import { resolve } from 'chart.js/src/helpers/helpers.options'

export const state = () => ({
  regions: [],
  projects: [],
  errors: [],
  sumProjectByCountry: [],
  evolutionAmountBySector: [],
  montants: [],
  montantParRegion: [],
  details: [],
  montantStatusParRegion: [],
  montantSecteurParRegion: [],
  montantBailleurParRegion: [],
  secteurs: [],
  bailleurs: [],
  montantsStatus: [],
  name: '',
})

export const mutations = {
  SET_NAME(state, payload) {
    state.name = payload
  },
  SET_MONTANT_STATUS(state, payload) {
    state.montantsStatus = payload
  },
  SET_BAILLEURS_DATA(state, payload) {
    state.bailleurs = payload
  },
  SET_SECTEURS_DATA(state, payload) {
    state.secteurs = payload
  },
  SET_MONTANT_BAILLEUR_PAR_REGION(state, payload) {
    state.montantBailleurParRegion = payload
  },
  SET_MONTANT_SECTEUR_PAR_REGION(state, payload) {
    state.montantSecteurParRegion = payload
  },
  SET_MONTANT_STATUS_PAR_REGION(state, payload) {
    state.montantStatusParRegion = payload
  },
  SET_DETAILS_DATA(state, payload) {
    state.details = payload
  },
  SET_EVOLUTION_AMOUNT_BY_SECTOR(state, payload) {
    state.evolutionAmountBySector = payload
  },
  SET_SUM_PROJECT_BY_COUNTRY(state, payload) {
    state.sumProjectByCountry = payload
  },
  SET_REGION_DATA(state, payload) {
    state.regions = payload
  },
  SET_PROJECTS_DATA(state, payload) {
    state.projects = payload
  },
  SET_ERRORS(state, payload) {
    state.errors = payload
  },
  SET_MONTANTS_DATA(state, payload) {
    state.montants = payload
  },
}

export const actions = {
  getBailleurs({ commit }, payload) {
    return new Promise((resolve, reject) => {
      this.$axios
        .get(`/organisation-list`)
        .then((response) => {
          commit('SET_BAILLEURS_DATA', response.data)
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
  getMontantParStatus({ commit }, payload) {
    return new Promise((resolve, reject) => {
      this.$axios
        .get(`/projects-status-year`)
        .then((response) => {
          let d1 = response.data
          let sumProject = d1.reduce((a, b) => a + parseInt(b['count']), 0)
          let labels = ['En cours', 'Términer']
          let sumScheduleProject = 0,
            sumDoneProject = 0
          d1.map((x) => {
            if (x.activity_status == '0' || x.activity_status == null)
              sumScheduleProject += parseInt(x.count)
            else sumDoneProject += parseInt(x.count)
          })
          const reponse = {
            series: [
              parseInt((sumScheduleProject * 100) / sumProject),
              parseInt((sumDoneProject * 100) / sumProject),
            ],
            options: {
              labels: labels,
            },
          }
          // console.log('reponse', reponse)
          commit('SET_MONTANT_STATUS', reponse)
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
  getMontantParStatusParRegion({ commit }, payload) {
    return new Promise((resolve, reject) => {
      this.$axios
        .get(`/projects-status-year-region`)
        .then((response) => {
          let data = response.data.filter((d) => d.region == payload)
          const jsonHelper = require('./../utils/jsonHelper')
          const amounts = jsonHelper.amountsStatus(data)
          commit('SET_MONTANT_STATUS_PAR_REGION', amounts)
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
  getMontantParBailleurParRegion({ commit }, payload) {
    return new Promise((resolve, reject) => {
      this.$axios
        .get(`/projects-budget-org-year-region`)
        .then((response) => {
          let data = response.data.filter((d) => d.region == payload)
          const jsonHelper = require('./../utils/jsonHelper')
          const amountsSectors = jsonHelper.amountsOrganisations(data)

          const final = {
            options: {
              chart: {
                id: 'bar-chart-montant-bailleur-par-region',
              },
              xaxis: {
                categories: amountsSectors.categories,
              },
            },
            series: amountsSectors.series,
          }
          commit('SET_MONTANT_BAILLEUR_PAR_REGION', final)
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

  getMontantParSecteurParRegion({ commit }, payload) {
    return new Promise((resolve, reject) => {
      this.$axios
        .get(`/projects-budget-sector-year-region`)
        .then((response) => {
          let data = response.data.filter((d) => d.region == payload)
          const jsonHelper = require('./../utils/jsonHelper')
          const amountsSectors = jsonHelper.amountsSectors(data)

          const final = {
            options: {
              chart: {
                id: 'line-chart-montant-secteur-par-region',
              },
              xaxis: {
                categories: amountsSectors.categories,
              },
            },
            series: amountsSectors.series,
          }
          commit('SET_MONTANT_SECTEUR_PAR_REGION', final)
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

  getMontantRegionsDataForChart({ commit }, payload) {
    return new Promise((resolve, reject) => {
      this.$axios
        .get(`/projects-budget-region-year`)
        .then((response) => {
          const data = response.data
          let regionList = [...new Set(data.map((x) => x.region))]
          regionList = regionList.filter((x) => x != null && x != undefined)
          let amountsSectors = []
          regionList.map((region) => {
            let val = { x: region, y: 0 }
            data.map((d) => {
              if (d.region == sector) val.y += parseInt(d.sum)
            })
            // val.y = new Intl.NumberFormat('en-US', {style: 'currency', currency: 'USD'}).format(val.y)
            amountsSectors.push(val)
          })
          const final = {
            options: {
              chart: {
                id: 'bar-chart-montant-region',
              },
              xaxis: {
                categories: regionList,
              },
            },
            series: [{data:amountsSectors}],
          }
          commit('SET_MONTANTS_DATA', final)
          resolve()
          // console.log(amountsCoutries)
          // console.log(state().regions)
          // console.log(state().montants)
        })
        .catch((error) => {
          if (error.response) {
            console.log('Error in Patient Data process...!')
          }
          commit('SET_ERRORS', 'Error in Patient Data process...!')
        })
    })
  },

  getEvolutionAmountBySectorData({ commit }, payload) {
    let search = payload ? payload : ''
    return new Promise((resolve, reject) => {
      this.$axios
        .get('/projects-budget-sector')
        .then((response) => {
          commit('SET_EVOLUTION_AMOUNT_BY_SECTOR', response.data)
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

  getSumProjetByCountriesData({ commit }, payload) {
    let search = payload ? payload : ''
    return new Promise((resolve, reject) => {
      this.$axios
        .get('/projects-budget-region')
        .then((response) => {
          commit('SET_SUM_PROJECT_BY_COUNTRY', response.data)
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
        .get(`/region-detail/${payload}`)
        .then((response) => {
          commit('SET_NAME', response.data.name)
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

  getDetailsData({ commit }, payload) {
    let search = payload ? payload : ''
    return new Promise((resolve, reject) => {
      this.$axios
        .get('/region-detail')
        .then((response) => {
          commit('SET_DETAILS_DATA', response.data)
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

  getRegionsData({ commit }, payload) {
    let search = payload ? payload : ''
    return new Promise((resolve, reject) => {
      this.$axios
        .get('/region-list')
        .then((response) => {
          const regionsData = response.data
          commit('SET_REGION_DATA', regionsData)
          resolve()
          // console.log(regionsData)
        })
        .catch((error) => {
          if (error.response) {
            console.log('Error in Patient Data process...!')
          }
          commit('SET_ERRORS', 'Error in Patient Data process...!')
        })
    })
  },

  getProjectsData({ commit }, payload) {
    return new Promise((resolve, reject) => {
      this.$axios
        .get(`/region-project-list/?q=${payload}`)
        .then((response) => {
          commit('SET_PROJECTS_DATA', response.data)
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
}
