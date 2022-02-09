import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import './plugins/element.js'
import { library } from '@fortawesome/fontawesome-svg-core'
import { faChevronCircleRight, faPlus, faMinus, faSignOutAlt } from '@fortawesome/free-solid-svg-icons'
import { faTimesCircle } from '@fortawesome/free-regular-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import './assets/css/main.css';
import axios from 'axios';

library.add(faChevronCircleRight, faPlus, faMinus, faSignOutAlt, faTimesCircle)

Vue.component('font-awesome-icon', FontAwesomeIcon)

Vue.config.productionTip = false

axios.defaults.baseURL = 'http://localhost:8000/';

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
