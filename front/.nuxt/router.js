import Vue from 'vue'
import Router from 'vue-router'
import { normalizeURL, decode } from 'ufo'
import { interopDefault } from './utils'
import scrollBehavior from './router.scrollBehavior.js'

const _b235e138 = () => interopDefault(import('..\\pages\\bailleurs\\index.vue' /* webpackChunkName: "pages/bailleurs/index" */))
const _1c00f76b = () => interopDefault(import('..\\pages\\error.vue' /* webpackChunkName: "pages/error" */))
const _8308ee10 = () => interopDefault(import('..\\pages\\projets\\index.vue' /* webpackChunkName: "pages/projets/index" */))
const _042c6720 = () => interopDefault(import('..\\pages\\regions\\index.vue' /* webpackChunkName: "pages/regions/index" */))
const _507f21ff = () => interopDefault(import('..\\pages\\test.vue' /* webpackChunkName: "pages/test" */))
const _1aa89f5e = () => interopDefault(import('..\\pages\\bailleurs\\projets\\_id.vue' /* webpackChunkName: "pages/bailleurs/projets/_id" */))
const _13e532af = () => interopDefault(import('..\\pages\\projets\\detail\\_id.vue' /* webpackChunkName: "pages/projets/detail/_id" */))
const _37216d15 = () => interopDefault(import('..\\pages\\regions\\projets\\_id.vue' /* webpackChunkName: "pages/regions/projets/_id" */))
const _4f8a4d96 = () => interopDefault(import('..\\pages\\index.vue' /* webpackChunkName: "pages/index" */))

const emptyFn = () => {}

Vue.use(Router)

export const routerOptions = {
  mode: 'history',
  base: '/',
  linkActiveClass: 'nuxt-link-active',
  linkExactActiveClass: 'nuxt-link-exact-active',
  scrollBehavior,

  routes: [{
    path: "/bailleurs",
    component: _b235e138,
    name: "bailleurs"
  }, {
    path: "/error",
    component: _1c00f76b,
    name: "error"
  }, {
    path: "/projets",
    component: _8308ee10,
    name: "projets"
  }, {
    path: "/regions",
    component: _042c6720,
    name: "regions"
  }, {
    path: "/test",
    component: _507f21ff,
    name: "test"
  }, {
    path: "/bailleurs/projets/:id?",
    component: _1aa89f5e,
    name: "bailleurs-projets-id"
  }, {
    path: "/projets/detail/:id?",
    component: _13e532af,
    name: "projets-detail-id"
  }, {
    path: "/regions/projets/:id?",
    component: _37216d15,
    name: "regions-projets-id"
  }, {
    path: "/",
    component: _4f8a4d96,
    name: "index"
  }],

  fallback: false
}

export function createRouter (ssrContext, config) {
  const base = (config._app && config._app.basePath) || routerOptions.base
  const router = new Router({ ...routerOptions, base  })

  // TODO: remove in Nuxt 3
  const originalPush = router.push
  router.push = function push (location, onComplete = emptyFn, onAbort) {
    return originalPush.call(this, location, onComplete, onAbort)
  }

  const resolve = router.resolve.bind(router)
  router.resolve = (to, current, append) => {
    if (typeof to === 'string') {
      to = normalizeURL(to)
    }
    return resolve(to, current, append)
  }

  return router
}
