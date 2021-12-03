import Vue from 'vue'
import Router from 'vue-router'
import { normalizeURL, decode } from 'ufo'
import { interopDefault } from './utils'
import scrollBehavior from './router.scrollBehavior.js'

const _58d41c3f = () => interopDefault(import('../pages/about.vue' /* webpackChunkName: "pages/about" */))
const _42e8ce80 = () => interopDefault(import('../pages/approche.vue' /* webpackChunkName: "pages/approche" */))
const _fdfe7cea = () => interopDefault(import('../pages/donors.vue' /* webpackChunkName: "pages/donors" */))
const _5930a446 = () => interopDefault(import('../pages/download.vue' /* webpackChunkName: "pages/download" */))
const _875bd58c = () => interopDefault(import('../pages/error.vue' /* webpackChunkName: "pages/error" */))
const _0aff0fec = () => interopDefault(import('../pages/projet.vue' /* webpackChunkName: "pages/projet" */))
const _55981b17 = () => interopDefault(import('../pages/projet1.vue' /* webpackChunkName: "pages/projet1" */))
const _03ad132f = () => interopDefault(import('../pages/sustainable.vue' /* webpackChunkName: "pages/sustainable" */))
const _094aafaa = () => interopDefault(import('../pages/donor/add.vue' /* webpackChunkName: "pages/donor/add" */))
const _5f386a46 = () => interopDefault(import('../pages/project/add.vue' /* webpackChunkName: "pages/project/add" */))
const _788bf704 = () => interopDefault(import('../pages/index.vue' /* webpackChunkName: "pages/index" */))

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
    component: _58d41c3f,
    name: "about"
  }, {
    path: "/approche",
    component: _42e8ce80,
    name: "approche"
  }, {
    path: "/donors",
    component: _fdfe7cea,
    name: "donors"
  }, {
    path: "/download",
    component: _5930a446,
    name: "download"
  }, {
    path: "/error",
    component: _875bd58c,
    name: "error"
  }, {
    path: "/projet",
    component: _0aff0fec,
    name: "projet"
  }, {
    path: "/projet1",
    component: _55981b17,
    name: "projet1"
  }, {
    path: "/sustainable",
    component: _03ad132f,
    name: "sustainable"
  }, {
    path: "/donor/add",
    component: _094aafaa,
    name: "donor-add"
  }, {
    path: "/project/add",
    component: _5f386a46,
    name: "project-add"
  }, {
    path: "/",
    component: _788bf704,
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
