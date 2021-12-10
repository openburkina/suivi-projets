import Vue from 'vue'
import Router from 'vue-router'
import { normalizeURL, decode } from 'ufo'
import { interopDefault } from './utils'
import scrollBehavior from './router.scrollBehavior.js'

const _3f5e2109 = () => interopDefault(import('../pages/about.vue' /* webpackChunkName: "pages/about" */))
const _5a4c1d76 = () => interopDefault(import('../pages/approche.vue' /* webpackChunkName: "pages/approche" */))
const _6bb75601 = () => interopDefault(import('../pages/donors.vue' /* webpackChunkName: "pages/donors" */))
const _7093f33c = () => interopDefault(import('../pages/download.vue' /* webpackChunkName: "pages/download" */))
const _ba47cbf8 = () => interopDefault(import('../pages/error.vue' /* webpackChunkName: "pages/error" */))
const _3591e700 = () => interopDefault(import('../pages/projet.vue' /* webpackChunkName: "pages/projet" */))
const _7c97d53e = () => interopDefault(import('../pages/projet1.vue' /* webpackChunkName: "pages/projet1" */))
const _9d624f0e = () => interopDefault(import('../pages/sustainable.vue' /* webpackChunkName: "pages/sustainable" */))
const _435d8118 = () => interopDefault(import('../pages/donor/add.vue' /* webpackChunkName: "pages/donor/add" */))
const _7e059027 = () => interopDefault(import('../pages/project/add.vue' /* webpackChunkName: "pages/project/add" */))
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
    path: "/about",
    component: _3f5e2109,
    name: "about"
  }, {
    path: "/approche",
    component: _5a4c1d76,
    name: "approche"
  }, {
    path: "/donors",
    component: _6bb75601,
    name: "donors"
  }, {
    path: "/download",
    component: _7093f33c,
    name: "download"
  }, {
    path: "/error",
    component: _ba47cbf8,
    name: "error"
  }, {
    path: "/projet",
    component: _3591e700,
    name: "projet"
  }, {
    path: "/projet1",
    component: _7c97d53e,
    name: "projet1"
  }, {
    path: "/sustainable",
    component: _9d624f0e,
    name: "sustainable"
  }, {
    path: "/donor/add",
    component: _435d8118,
    name: "donor-add"
  }, {
    path: "/project/add",
    component: _7e059027,
    name: "project-add"
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
