import Vue from 'vue'
import Vuex from 'vuex'
import signup from './modules/signup'
import auth from './modules/auth'
Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    signup,
    auth
  }
})
