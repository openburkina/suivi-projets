import Vue from 'vue'
import Router from 'vue-router'
import { normalizeURL, decode } from 'ufo'
import { interopDefault } from './utils'
import scrollBehavior from './router.scrollBehavior.js'

const _8efa0320 = () => interopDefault(import('..\\pages\\about.vue' /* webpackChunkName: "pages/about" */))
const _034cf2af = () => interopDefault(import('..\\pages\\approche.vue' /* webpackChunkName: "pages/approche" */))
const _e58f3800 = () => interopDefault(import('..\\pages\\backers\\index.vue' /* webpackChunkName: "pages/backers/index" */))
const _b235e138 = () => interopDefault(import('..\\pages\\bailleurs\\index.vue' /* webpackChunkName: "pages/bailleurs/index" */))
const _af9b08e6 = () => interopDefault(import('..\\pages\\currentProject.vue' /* webpackChunkName: "pages/currentProject" */))
const _172e257a = () => interopDefault(import('..\\pages\\donors.vue' /* webpackChunkName: "pages/donors" */))
const _1994c875 = () => interopDefault(import('..\\pages\\download.vue' /* webpackChunkName: "pages/download" */))
const _1c00f76b = () => interopDefault(import('..\\pages\\error.vue' /* webpackChunkName: "pages/error" */))
const _210eb33b = () => interopDefault(import('..\\pages\\projects\\index.vue' /* webpackChunkName: "pages/projects/index" */))
const _264b8be8 = () => interopDefault(import('..\\pages\\projects1\\index.vue' /* webpackChunkName: "pages/projects1/index" */))
const _2dfd3147 = () => interopDefault(import('..\\pages\\projects2\\index.vue' /* webpackChunkName: "pages/projects2/index" */))
const _35aed6a6 = () => interopDefault(import('..\\pages\\projects3\\index.vue' /* webpackChunkName: "pages/projects3/index" */))
const _dea4480e = () => interopDefault(import('..\\pages\\projet.vue' /* webpackChunkName: "pages/projet" */))
const _8308ee10 = () => interopDefault(import('..\\pages\\projets\\index.vue' /* webpackChunkName: "pages/projets/index" */))
const _6d8866c0 = () => interopDefault(import('..\\pages\\sustainable.vue' /* webpackChunkName: "pages/sustainable" */))
const _13e532af = () => interopDefault(import('..\\pages\\projets\\detail\\_id.vue' /* webpackChunkName: "pages/projets/detail/_id" */))
const _dd4ef130 = () => interopDefault(import('..\\pages\\works\\_works.vue' /* webpackChunkName: "pages/works/_works" */))
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
    path: "/about",
    component: _8efa0320,
    name: "about"
  }, {
    path: "/approche",
    component: _034cf2af,
    name: "approche"
  }, {
    path: "/backers",
    component: _e58f3800,
    name: "backers"
  }, {
    path: "/bailleurs",
    component: _b235e138,
    name: "bailleurs"
  }, {
    path: "/currentProject",
    component: _af9b08e6,
    name: "currentProject"
  }, {
    path: "/donors",
    component: _172e257a,
    name: "donors"
  }, {
    path: "/download",
    component: _1994c875,
    name: "download"
  }, {
    path: "/error",
    component: _1c00f76b,
    name: "error"
  }, {
    path: "/projects",
    component: _210eb33b,
    name: "projects"
  }, {
    path: "/projects1",
    component: _264b8be8,
    name: "projects1"
  }, {
    path: "/projects2",
    component: _2dfd3147,
    name: "projects2"
  }, {
    path: "/projects3",
    component: _35aed6a6,
    name: "projects3"
  }, {
    path: "/projet",
    component: _dea4480e,
    name: "projet"
  }, {
    path: "/projets",
    component: _8308ee10,
    name: "projets"
  }, {
    path: "/sustainable",
    component: _6d8866c0,
    name: "sustainable"
  }, {
    path: "/projets/detail/:id?",
    component: _13e532af,
    name: "projets-detail-id"
  }, {
    path: "/works/:works?",
    component: _dd4ef130,
    name: "works-works"
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
