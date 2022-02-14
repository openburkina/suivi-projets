import Vue from 'vue'
import Router from 'vue-router'
import { normalizeURL, decode } from 'ufo'
import { interopDefault } from './utils'
import scrollBehavior from './router.scrollBehavior.js'

const _e025428c = () => interopDefault(import('../pages/bailleurs/index.vue' /* webpackChunkName: "pages/bailleurs/index" */))
const _ba47cbf8 = () => interopDefault(import('../pages/error.vue' /* webpackChunkName: "pages/error" */))
const _0f8f64e6 = () => interopDefault(import('../pages/projets/index.vue' /* webpackChunkName: "pages/projets/index" */))
const _a293bc84 = () => interopDefault(import('../pages/regions/index.vue' /* webpackChunkName: "pages/regions/index" */))
const _54d8c846 = () => interopDefault(import('../pages/test.vue' /* webpackChunkName: "pages/test" */))
const _3ea42456 = () => interopDefault(import('../pages/regions/test.vue' /* webpackChunkName: "pages/regions/test" */))
const _eed78878 = () => interopDefault(import('../pages/projets/details/_id/index.vue' /* webpackChunkName: "pages/projets/details/_id/index" */))
const _5f15fbce = () => interopDefault(import('../pages/index.vue' /* webpackChunkName: "pages/index" */))

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
    component: _e025428c,
    name: "bailleurs"
  }, {
    path: "/error",
    component: _ba47cbf8,
    name: "error"
  }, {
    path: "/projets",
    component: _0f8f64e6,
    name: "projets"
  }, {
    path: "/regions",
    component: _a293bc84,
    name: "regions"
  }, {
    path: "/test",
    component: _54d8c846,
    name: "test"
  }, {
    path: "/regions/test",
    component: _3ea42456,
    name: "regions-test"
  }, {
    path: "/projets/details/:id",
    component: _eed78878,
    name: "projets-details-id"
  }, {
    path: "/",
    component: _5f15fbce,
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
