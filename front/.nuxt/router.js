import Vue from 'vue'
import Router from 'vue-router'
import { normalizeURL, decode } from 'ufo'
import { interopDefault } from './utils'
import scrollBehavior from './router.scrollBehavior.js'

const _9d1c6d12 = () => interopDefault(import('../pages/about.vue' /* webpackChunkName: "pages/about" */))
const _d02d1370 = () => interopDefault(import('../pages/approche.vue' /* webpackChunkName: "pages/approche" */))
const _d5cb3968 = () => interopDefault(import('../pages/backers/index.vue' /* webpackChunkName: "pages/backers/index" */))
const _748baf34 = () => interopDefault(import('../pages/currentProject.vue' /* webpackChunkName: "pages/currentProject" */))
const _3c18bb53 = () => interopDefault(import('../pages/donors.vue' /* webpackChunkName: "pages/donors" */))
const _a39d67e4 = () => interopDefault(import('../pages/download.vue' /* webpackChunkName: "pages/download" */))
const _14efc272 = () => interopDefault(import('../pages/error.vue' /* webpackChunkName: "pages/error" */))
const _7ca49983 = () => interopDefault(import('../pages/projects/index.vue' /* webpackChunkName: "pages/projects/index" */))
const _7dac8eb8 = () => interopDefault(import('../pages/projects1/index.vue' /* webpackChunkName: "pages/projects1/index" */))
const _94cf1c5c = () => interopDefault(import('../pages/projet.vue' /* webpackChunkName: "pages/projet" */))
const _4a1c1332 = () => interopDefault(import('../pages/sustainable.vue' /* webpackChunkName: "pages/sustainable" */))
const _77f53636 = () => interopDefault(import('../pages/works/_works.vue' /* webpackChunkName: "pages/works/_works" */))
const _5dacb788 = () => interopDefault(import('../pages/index.vue' /* webpackChunkName: "pages/index" */))

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
    component: _9d1c6d12,
    name: "about"
  }, {
    path: "/approche",
    component: _d02d1370,
    name: "approche"
  }, {
    path: "/backers",
    component: _d5cb3968,
    name: "backers"
  }, {
    path: "/currentProject",
    component: _748baf34,
    name: "currentProject"
  }, {
    path: "/donors",
    component: _3c18bb53,
    name: "donors"
  }, {
    path: "/download",
    component: _a39d67e4,
    name: "download"
  }, {
    path: "/error",
    component: _14efc272,
    name: "error"
  }, {
    path: "/projects",
    component: _7ca49983,
    name: "projects"
  }, {
    path: "/projects1",
    component: _7dac8eb8,
    name: "projects1"
  }, {
    path: "/projet",
    component: _94cf1c5c,
    name: "projet"
  }, {
    path: "/sustainable",
    component: _4a1c1332,
    name: "sustainable"
  }, {
    path: "/works/:works?",
    component: _77f53636,
    name: "works-works"
  }, {
    path: "/",
    component: _5dacb788,
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
