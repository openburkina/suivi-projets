import axios from 'axios'
import { pieStatAdapter, lineStatAdapter, barStatAdapter } from '~/helpers/Adapters'
export const state = () => ({
    particularName:'',
    regionName:'',
//API BAILLEUR,REGION,PROJET
    projectList : [],
    projectDetails : [],
    projectDetailsIndicateur : [],
    projectDetailsTransaction : [],
    projectDetailsChild : [],
    organisationList : [],
    organisationDetails : [],
    organisationTransactionE : [],
    organisationTransactionR : [],
    regionList : [],
    regionProject : [],
    regionTransaction : [],
    regionDecaissement : [],
    homeRegionValues: [],
//END
//STATISTIQUE GRAPHIQUE
    organismePieStats: {'labels': [], 'data': []},
    organismeBarOneStats: {'labels': [], 'data': []},
    organismeBarTwoStats: {'labels': [], 'data': []},
    organismeLineStats: {'labels': [], 'data': []},
    homePieStats: {'labels': [], 'data': []},
    homeBarOneStats: {'labels': [], 'data': []},
    homeBarTwoStats: {'labels': [], 'data': []},
    homeLineStats: {'labels': [], 'data': []},
    regionPieStats: {'labels': [], 'data': []},
    regionBarOneStats: {'labels': [], 'data': []},
    regionBarTwoStats: {'labels': [], 'data': []},
    regionLineStats: {'labels': [], 'data': []},
    
//END
  })

export const mutations = {
//Setter Stats Tableau
    setProjectList(state, payload) {
        state.projectList = payload
    },
    setProjectDetails(state, payload) {
        state.projectDetails = payload
    },
    setProjectDetailsTransaction(state, payload) {
        state.projectDetailsTransaction = payload
    },
    setProjectDetailsIndicateur(state, payload) {
        state.projectDetailsIndicateur = payload
    },
    setProjectDetailsChild(state, payload) {
        state.projectDetailsChild = payload
    },
    setOrganisationList(state, payload) {
        state.organisationList = payload
    },
    setOrganisationDetails(state, payload) {
        state.organisationDetails = payload
    },
    setOrganisationTransactionR(state, payload) {
        state.organisationTransactionR = payload
    },
    setOrganisationTransactionE(state, payload) {
        state.organisationTransactionE = payload
    },
    setRegionList(state, payload) {
        state.regionList = payload
    },
    setRegionProject(state, payload) {
        state.regionProject = payload
    },
    setRegionTransaction(state, payload) {
        state.regionTransaction = payload
    },
    setRegionDecaissement(state, payload) {
        state.regionDecaissement = payload
    },
    setHomeRegionValues(state, payload) {
        state.homeRegionValues = payload.data
    },
//End Stats Tableau

//Start Stat Graphique Setters
    setOrganismePieStats(state, payload) {
        state.organismePieStats = payload.data
    },
    setOrganismeBarOneStats(state, payload) {
        state.organismeBarOneStats = payload.data
    },
    setOrganismeBarTwoStats(state, payload) {
        state.organismeBarTwoStats = payload.data
    },
    setOrganismeLineStats(state, payload) {
        state.organismeLineStats = payload.data
    },

    setHomePieStats(state, payload) {
        state.homePieStats = payload.data
    },
    setHomeBarOneStats(state, payload) {
        state.homeBarOneStats = payload.data
    },
    setHomeBarTwoStats(state, payload) {
        state.homeBarTwoStats = payload.data
    },
    setHomeLineStats(state, payload) {
        state.homeLineStats = payload.data
    },
    setRegionPieStats(state, payload) {
        state.regionPieStats = payload.data
    },
    setRegionBarOneStats(state, payload) {
        state.regionBarOneStats = payload.data
    },
    setRegionBarTwoStats(state, payload) {
        state.regionBarTwoStats = payload.data
    },
    setRegionLineStats(state, payload) {
        state.regionLineStats = payload.data
    },
//End

}
export const actions = {
    //Projets
    async fetchProjects({ commit }) {
        await axios.get(
            `http://localhost:8000/api/projets`
        ).then(res => {
            commit("setProjectList", res.data)
        })
    },

    async fetchProjectsDetails({ commit },id) {
        await axios.get(
            `http://localhost:8000/api/projets/${id}/details`
        ).then(res => {
            console.log(res.data)
            commit("setProjectDetails", res.data)
        })
    },

    async fetchProjectsDetailsTransaction({ commit },id) {
        await axios.get(
            `http://localhost:8000/api/projets/${id}/transaction`
        ).then(res => {
            commit("setProjectDetailsTransaction", res.data)
        })
    },

    async fetchProjectsDetailsIndicateur({ commit },id) {
        await axios.get(
            `http://localhost:8000/api/projets/${id}/indicateur`
        ).then(res => {
            commit("setProjectDetailsIndicateur", res.data)
        })
    },

    async fetchProjectsDetailsChild({ commit },id) {
        await axios.get(
            `http://localhost:8000/api/projets/${id}/child`
        ).then(res => {
            commit("setProjectDetailsChild", res.data)
        })
    },

    //End
    //Organisme
    async fetchOrganisation({ commit }) {
        await axios.get(
            `http://localhost:8000/api/projets/organisation`
        ).then(res => {
            commit("setOrganisationList", res.data)
        })
    },

    async fetchOrganisationDetails({ commit },id) {
        await axios.get(
            `http://localhost:8000/api/projets/${id}/organisation/activite`
        ).then(res => {
            commit("setOrganisationDetails", res.data)
        })
    },

    async fetchOrganisationTransactionR({ commit },id) {
        await axios.get(
            `http://localhost:8000/api/projets/${id}/organisation/transactionr`
        ).then(res => {
            commit("setOrganisationTransactionR", res.data)
        })
    },

    async fetchOrganisationTransactionE({ commit },id) {
        await axios.get(
            `http://localhost:8000/api/projets/${id}/organisation/transactione`
        ).then(res => {
            commit("setOrganisationTransactionE", res.data)
        })
    },
    //End
    //Region
    async fetchRegion({ commit }) {
        await axios.get(
            `http://localhost:8000/api/projets/region`
        ).then(res => {
            commit("setRegionList", res.data)
        })
    },

    async fetchRegionProject({ commit },region_id) {
        await axios.get(
            `http://localhost:8000/api/projets/${region_id}/region/activite`
        ).then(res => {
            commit("setRegionProject", res.data)
        })
    },

    async fetchRegionTransaction({ commit },region_id) {
        await axios.get(
            `http://localhost:8000/api/projets/${region_id}/region/transaction`
        ).then(res => {
            commit("setRegionTransaction", res.data)
        })
    },

    async fetchRegionDecaissement({ commit },region_id) {
        await axios.get(
            `http://localhost:8000/api/projets/${region_id}/region/decaissement`
        ).then(res => {
            commit("setRegionDecaissement", res.data)
        })
    },
    //End

        // Organisme Stats
    async fetchOrganismePieStats({ commit }, {buyer_id, year }) {
        await axios.get(
            `http://localhost:8000/api/projets/${buyer_id}/organisation/by_status?year=${year}`
        ).then(res => {
            commit("setOrganismePieStats", {name: "pie", data : pieStatAdapter(res.data)})
        })
    },
    async fetchOrganismeBarOneStats({ commit }, { buyer_id, year }) {
        axios.get(
            `http://localhost:8000/api/projets/${buyer_id}/organisation/by_regiontransact?year=${year}`
        ).then(res => {
            commit("setOrganismeBarOneStats", {name: "barOne", data : barStatAdapter(res.data)})
        })
    },
    async fetchOrganismeBarTwoStats({ commit }, {buyer_id, year }) {
        axios.get(
            `http://localhost:8000/api/projets/${buyer_id}/organisation/by_region?year=${year}`
        ).then(res => {
            commit("setOrganismeBarTwoStats", {name: "barTwo", data : barStatAdapter(res.data)})
        })
    },
    async fetchOrganismeLineStats({ commit }, {buyer_id, start_year, end_year }) {
        await axios.get(
            `http://localhost:8000/api/projets/${buyer_id}/organisation/by_sector?start_year=${start_year}&end_year=${end_year}`
        ).then(res => {
            commit("setOrganismeLineStats", {name: "line", data : lineStatAdapter(res.data, start_year, end_year)})
        })
    },
        // End Organisme Stats
    
        // Home Stats
        async fetchHomeRegionValues({ commit }) {
            await axios.get(
                `http://localhost:8000/api/projets/homeactivity/by_regiontransaction`
            ).then(res => {
                commit("setHomeRegionValues", {'data': res.data})
            })
        },
    
        async fetchHomePieStats({ commit }, {year }) {
            await axios.get(
                `http://localhost:8000/api/projets/homeactivity/by_status?year=${year}`
            ).then(res => {
                commit("setHomePieStats", {name: "pie", data : pieStatAdapter(res.data)})
            })
        },
        async fetchHomeBarOneStats({ commit }, {year }) {
            axios.get(
                `http://localhost:8000/api/projets/homeactivity/by_regiontransact?year=${year}`
            ).then(res => {
                commit("setHomeBarOneStats", {name: "barOne", data : barStatAdapter(res.data)})
            })
        },
        async fetchHomeBarTwoStats({ commit }, {year }) {
            axios.get(
                `http://localhost:8000/api/projets/homeactivity/by_sectortransact?year=${year}`
            ).then(res => {
                commit("setHomeBarTwoStats", {name: "barTwo", data : barStatAdapter(res.data)})
            })
        },
        async fetchHomeLineStats({ commit }, {start_year, end_year }) {
            await axios.get(
                `http://localhost:8000/api/projets/homeactivity/by_sector?start_year=${start_year}&end_year=${end_year}`
            ).then(res => {
                commit("setHomeLineStats", {name: "line", data : lineStatAdapter(res.data, start_year, end_year)})
            })
        },
        // End Home Stats

        // Region Stats
        async fetchRegionPieStats({ commit }, {region_id,year }) {
            await axios.get(
                `http://localhost:8000/api/projets/${region_id}/region/by_status?year=${year}`
            ).then(res => {
                commit("setRegionPieStats", {name: "pie", data : pieStatAdapter(res.data)})
            })
        },
        async fetchRegionBarOneStats({ commit }, {region_id,year }) {
            axios.get(
                `http://localhost:8000/api/projets/${region_id}/region/by_condition?year=${year}`
            ).then(res => {
                commit("setRegionBarOneStats", {name: "barOne", data : barStatAdapter(res.data)})
            })
        },
        async fetchRegionBarTwoStats({ commit }, {region_id,year }) {
            axios.get(
                `http://localhost:8000/api/projets/${region_id}/region/by_sectortransact?year=${year}`
            ).then(res => {
                commit("setRegionBarTwoStats", {name: "barTwo", data : barStatAdapter(res.data)})
            })
        },
        async fetchRegionLineStats({ commit }, {region_id,start_year, end_year }) {
            await axios.get(
                `http://localhost:8000/api/projets/${region_id}/region/by_sector?start_year=${start_year}&end_year=${end_year}`
            ).then(res => {
                commit("setRegionLineStats", {name: "line", data : lineStatAdapter(res.data, start_year, end_year)})
            })
        },
        // End Region Stats
        
}
export const getters = {}




// Colaboration : 
// etude : doc,url