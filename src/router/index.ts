import Vue from 'vue'
import VueRouter, { RouteConfig } from 'vue-router'
import SignUp from '../components/SignUp.vue'
import CreditProposals from '../views/CreditProposals.vue'

Vue.use(VueRouter)

const routes: Array<RouteConfig> = [

  {
    path: '/',
    name: 'Home',

    component: () => import(/* webpackChunkName: "about" */ '../views/Home.vue')
  },
  {
    path: '/sign-up',
    name: 'SignUp',

    component: SignUp
  },
  {
    path: '/proposals',
    name: 'proposals',

    component: CreditProposals
  }
]

const router = new VueRouter({
  mode: 'history',
  routes
})

export default router
