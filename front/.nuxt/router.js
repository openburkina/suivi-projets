import Vue from 'vue'
import Router from 'vue-router'
import { normalizeURL, decode } from 'ufo'
import { interopDefault } from './utils'
import scrollBehavior from './router.scrollBehavior.js'

const _3f5e2109 = () => interopDefault(import('../pages/about.vue' /* webpackChunkName: "pages/about" */))
const _5a4c1d76 = () => interopDefault(import('../pages/approche.vue' /* webpackChunkName: "pages/approche" */))
const _47c708de = () => interopDefault(import('../pages/backers/index.vue' /* webpackChunkName: "pages/backers/index" */))
const _68a23514 = () => interopDefault(import('../pages/currentProject.vue' /* webpackChunkName: "pages/currentProject" */))
const _6bb75601 = () => interopDefault(import('../pages/donors.vue' /* webpackChunkName: "pages/donors" */))
const _7093f33c = () => interopDefault(import('../pages/download.vue' /* webpackChunkName: "pages/download" */))
const _ba47cbf8 = () => interopDefault(import('../pages/error.vue' /* webpackChunkName: "pages/error" */))
const _1f8ca631 = () => interopDefault(import('../pages/projects/index.vue' /* webpackChunkName: "pages/projects/index" */))
const _7b4341b6 = () => interopDefault(import('../pages/projects1/index.vue' /* webpackChunkName: "pages/projects1/index" */))
const _1027f477 = () => interopDefault(import('../pages/projects2/index.vue' /* webpackChunkName: "pages/projects2/index" */))
const _b5e6b190 = () => interopDefault(import('../pages/projects3/index.vue' /* webpackChunkName: "pages/projects3/index" */))
const _3591e700 = () => interopDefault(import('../pages/projet.vue' /* webpackChunkName: "pages/projet" */))
const _9d624f0e = () => interopDefault(import('../pages/sustainable.vue' /* webpackChunkName: "pages/sustainable" */))
const _6d349664 = () => interopDefault(import('../pages/works/_works.vue' /* webpackChunkName: "pages/works/_works" */))
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
    path: "/backers",
    component: _47c708de,
    name: "backers"
  }, {
    path: "/currentProject",
    component: _68a23514,
    name: "currentProject"
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
    path: "/projects",
    component: _1f8ca631,
    name: "projects"
  }, {
    path: "/projects1",
    component: _7b4341b6,
    name: "projects1"
  }, {
    path: "/projects2",
    component: _1027f477,
    name: "projects2"
  }, {
    path: "/projects3",
    component: _b5e6b190,
    name: "projects3"
  }, {
    path: "/projet",
    component: _3591e700,
    name: "projet"
  }, {
    path: "/sustainable",
    component: _9d624f0e,
    name: "sustainable"
  }, {
    path: "/works/:works?",
    component: _6d349664,
    name: "works-works"
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
