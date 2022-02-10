const state = {
  idCompany: null,
  name: null,
};

const getters = {

};

const actions = {

};

const mutations = {
  setIsLogged(state: any, payload: any) {
    state.isLogged = payload.isLogged
  },
  setUserName(state: any, payload: any) {
    state.name = payload.name
  },
  setOffer(state: any, payload: any) {
    state.offer = payload.offer
  },
  setIdCompany(state: any, payload: any) {
    state.idCompany = payload.idCompany
  },
};

export default {
  state,
  getters,
  actions,
  mutations
};