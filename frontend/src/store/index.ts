import Vue from 'vue'
import Vuex from 'vuex'
import signup from './modules/signup'
import user from './modules/user'
Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    signup,
    user
  }
})
