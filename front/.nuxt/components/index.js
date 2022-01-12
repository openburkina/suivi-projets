export { default as BarChart } from '../..\\components\\barChart.vue'
export { default as BarChartContent } from '../..\\components\\barChartContent.vue'
export { default as ButtonGroup } from '../..\\components\\buttonGroup.vue'
export { default as ButtonTitle } from '../..\\components\\buttonTitle.vue'
export { default as Caroussel } from '../..\\components\\caroussel.vue'
export { default as Error } from '../..\\components\\error.vue'
export { default as Footer } from '../..\\components\\footer.vue'
export { default as Leaflet } from '../..\\components\\leaflet.vue'
export { default as LineChart } from '../..\\components\\lineChart.vue'
export { default as LineChartContent } from '../..\\components\\lineChartContent.vue'
export { default as MenuPage } from '../..\\components\\menu-page.vue'
export { default as MenuProjectsPage } from '../..\\components\\menu-projects-page.vue'
export { default as MenuProjects } from '../..\\components\\menu-projects.vue'
export { default as Menu } from '../..\\components\\menu.vue'
export { default as Parallax } from '../..\\components\\parallax.vue'
export { default as ParallaxContent } from '../..\\components\\ParallaxContent.vue'
export { default as PieChart } from '../..\\components\\pieChart.vue'
export { default as PieChartContent } from '../..\\components\\pieChartContent.vue'
export { default as ResponsiveButtonGroup } from '../..\\components\\responsiveButtonGroup.vue'
export { default as Tabs } from '../..\\components\\tabs.vue'
export { default as TabsHomePage } from '../..\\components\\tabsHomePage.vue'
export { default as Title } from '../..\\components\\title.vue'
export { default as Travaux } from '../..\\components\\travaux.vue'
export { default as TravauxContentDone } from '../..\\components\\travauxContentDone.vue'
export { default as TravauxContentInprogress } from '../..\\components\\travauxContentInprogress.vue'

// nuxt/nuxt.js#8607
function wrapFunctional(options) {
  if (!options || !options.functional) {
    return options
  }

  const propKeys = Array.isArray(options.props) ? options.props : Object.keys(options.props || {})

  return {
    render(h) {
      const attrs = {}
      const props = {}

      for (const key in this.$attrs) {
        if (propKeys.includes(key)) {
          props[key] = this.$attrs[key]
        } else {
          attrs[key] = this.$attrs[key]
        }
      }

      return h(options, {
        on: this.$listeners,
        attrs,
        props,
        scopedSlots: this.$scopedSlots,
      }, this.$slots.default)
    }
  }
}
