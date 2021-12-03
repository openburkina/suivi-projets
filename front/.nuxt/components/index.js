export { default as ParallaxContent } from '../../components/ParallaxContent.vue'
export { default as ButtonGroup } from '../../components/buttonGroup.vue'
export { default as Error } from '../../components/error.vue'
export { default as Footer } from '../../components/footer.vue'
export { default as Leaflet } from '../../components/leaflet.vue'
export { default as Parallax } from '../../components/parallax.vue'
export { default as ResponsiveButtonGroup } from '../../components/responsiveButtonGroup.vue'
export { default as Tabs } from '../../components/tabs.vue'

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
