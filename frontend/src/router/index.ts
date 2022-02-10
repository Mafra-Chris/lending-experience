import Vue from 'vue'
import VueRouter, { RouteConfig } from 'vue-router'
import SignUp from '../views/SignUp.vue'
import CreditProposals from '../views/CreditProposals.vue'

Vue.use(VueRouter)

const routes: Array<RouteConfig> = [

  {
    path: '/',
    name: 'SignUp',

    component: () => import('../views/SignUp.vue')
  },
  {
    path: '/chosen',
    name: 'Chosen',

    component: () => import('../views/Home.vue')
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
