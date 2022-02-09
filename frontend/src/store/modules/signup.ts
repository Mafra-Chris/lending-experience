
const state = {
  name: '',
  cnpj: '',
  website: '',
  segmentOption: '',
  monthlyRevenue: 0,
  moneyPurpose: '',
  email: '',
  isTermsChecked: false,
  progressPerc: 0,
  currentStep: 0
};

const getters = {

};

const actions = {

};

const mutations = {
  setName(state: any, payload: any) {
    state.name = payload.name
  },
  setCnpj(state: any, payload: any) {
    state.cnpj = payload.cnpj
  },
  setWebsite(state: any, payload: any) {
    state.website = payload.website
  },
  setSegmentOption(state: any, payload: any) {
    state.segmentOption = payload.segmentOption
  },
  setMonthlyRevenue(state: any, payload: any) {
    state.monthlyRevenue = payload.monthlyRevenue
  },
  setMoneyPurpose(state: any, payload: any) {
    state.moneyPurpose = payload.moneyPurpose
  },
  setIsTermsChecked(state: any, payload: any) {
    state.termsChecked = payload.termsChecked
  },
  setEmail(state: any, payload: any) {
    state.email = payload.email
  },
  setProgressPerc(state: any, payload: any) {
    state.progressPerc = payload.progressPerc
  },

  incrementCurrentStep() {
    if (state.currentStep < 2)
      state.currentStep++
  },
  decrementCurrentStep() {
    if (state.currentStep > 0) {
      state.currentStep--
    }
  }
};


export default {
  state,
  getters,
  actions,
  mutations
};