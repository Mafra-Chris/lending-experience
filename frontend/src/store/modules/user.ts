const state = {
  isLogged: false,
  name: null,
  offer: {
    id: 0,
    installments: 12
  }
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
};

export default {
  state,
  getters,
  actions,
  mutations
};