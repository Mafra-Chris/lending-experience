const state = {
  isLogged: false,
  name: null,
  offer: {
    id: 0,
    installments: 0
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
  setName(state: any, payload: any) {
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