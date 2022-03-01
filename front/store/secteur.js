export const state = () => ({
  montants: [],
  errors: [],
})

export const mutations = {
  SET_MONTANTS_DATA(state, payload) {
    state.montants = payload
  },
  SET_ERRORS(state, payload) {
    state.errors = payload
  },
}

const getYears = (data) => {
  return [...new Set(data.map(x => x.year))].sort();
}

const getSectors= (data) => {
  return [...new Set(data.map(x => x.sector))];
}

const myFilter = (data, sector, year) => {
  let val = 0;
  data.map(d => {
    if (d.sector==sector && d.year==year){
      val = parseInt(d.sum);
    }
  });
  return val;
}

const getSeries = (data) => {
  let tab = [];
  getSectors(data).map(sector => {
    let value = {name: sector};
    let temp = [];
    getYears(data).map(year => {
      let sum = myFilter(data, sector, year);
      temp.push(sum);
    });
    value = {...value, data: temp};
    tab.push(value);
  });
  return tab;
}
export const actions = {
  getMontantSecteursDataForChart({ commit }, payload) {
    return new Promise((resolve, reject) => {
      this.$axios
        .get(`/projects-budget-sector`)
        .then((response) => {
          const data = response.data;
          
          const final = {
            options: {
              chart: {
                id: 'line-chart-montant-secteur',
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

  getMontantSecteursData({ commit }, payload) {
    return new Promise((resolve, reject) => {
      this.$axios
        .get(`/projects-budget-sector`)
        .then((response) => {
          commit('SET_MONTANTS_DATA', response.data)
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
