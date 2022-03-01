export const state = () => ({
  regions: [],
  projects: [],
  errors: [],
  sumProjectByCountry: [],
  evolutionAmountBySector: [],
  montants: [],
})

export const mutations = {
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


const getYears = (data) => {
  return [...new Set(data.map(x => x.year))].sort();
}

const getRegions= (data) => {
  return [...new Set(data.map(x => x.region))];
}

const myFilter = (data, region, year) => {
  let val = 0;
  data.map(d => {
    if (d.region==region && d.year==year){
      val = parseInt(d.sum);
    }
  });
  return val;
}

const getSeries = (data) => {
  let tab = [];
  getRegions(data).map(region => {
    let value = {name: region};
    let temp = [];
    getYears(data).map(year => {
      let sum = myFilter(data, region, year);
      temp.push(sum);
    });
    value = {...value, data: temp};
    tab.push(value);
  });
  return tab;
}


export const actions = {
  getMontantRegionsDataForChart({ commit }, payload) {
    return new Promise((resolve, reject) => {
      this.$axios
        .get(`/projects-budget-region-year`)
        .then((response) => {
          const data = response.data;
          
          const final = {
            options: {
              chart: {
                id: 'bar-chart-montant-region',
              },
              xaxis: {
                categories: getYears(data),
              }
            },
            series: getSeries(data),
          }
          commit('SET_MONTANTS_DATA', final)
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

  getEvolutionAmountBySectorData({ commit }, payload) {
    let search = payload ? payload : ''
    return new Promise((resolve, reject) => {
      this.$axios.get('/projects-budget-sector').then((response) => {
        commit('SET_EVOLUTION_AMOUNT_BY_SECTOR', response.data)
        resolve()
      }).catch((error)=> {
        if(error.response){
          console.log("Error in Patient Data process...!")
        }
        commit('SET_ERRORS', "Error in Patient Data process...!")
      })
    })
  },
  getSumProjetByCountriesData({ commit }, payload) {
    let search = payload ? payload : ''
    return new Promise((resolve, reject) => {
      this.$axios.get('/projects-budget-region').then((response) => {
        commit('SET_SUM_PROJECT_BY_COUNTRY', response.data)
        resolve()
      }).catch((error)=> {
        if(error.response){
          console.log("Error in Patient Data process...!")
        }
        commit('SET_ERRORS', "Error in Patient Data process...!")
      })
    })
  },
  getRegionsData({ commit }, payload) {
    let search = payload ? payload : ''
    return new Promise((resolve, reject) => {
      this.$axios.get('/region-list').then((response) => {
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
      this.$axios.get(`/region-project-list/?q=${payload}`).then((response)=> {
        commit('SET_PROJECTS_DATA', response.data)
        resolve()
        console.log(`/region-project-list/?q=${payload}`)
      }).catch((error)=> {
        if(error.response){
          console.log("Error in Patient Data process...!")
        }
        commit('SET_ERRORS', "Error in Patient Data process...!")
      })
    })
  },
}
