export { default as BarChart } from '../..\\components\\barChart.vue'
export { default as BarChartMontantParRegion } from '../..\\components\\barChartMontantParRegion.vue'
export { default as BarChartMontantParRegionParBailleur } from '../..\\components\\barChartMontantParRegionParBailleur.vue'
export { default as BarChartMontantParRegionParRegion } from '../..\\components\\barChartMontantParRegionParRegion.vue'
export { default as BarChartMontantParSecteur } from '../..\\components\\barChartMontantParSecteur.vue'
export { default as BarChartMontantParSecteurParBailleur } from '../..\\components\\barChartMontantParSecteurParBailleur.vue'
export { default as BarChartMontantParSecteurParRegion } from '../..\\components\\barChartMontantParSecteurParRegion.vue'
export { default as Caroussel } from '../..\\components\\caroussel.vue'
export { default as DatatableProjets } from '../..\\components\\datatableProjets.vue'
export { default as DatatableRegions } from '../..\\components\\datatableRegions.vue'
export { default as DonutChart } from '../..\\components\\donutChart.vue'
export { default as DonutChartStatutProjet } from '../..\\components\\donutChartStatutProjet.vue'
export { default as DonutChartStatutProjetParBailleur } from '../..\\components\\donutChartStatutProjetParBailleur.vue'
export { default as DonutChartStatutProjetParRegion } from '../..\\components\\donutChartStatutProjetParRegion.vue'
export { default as Error } from '../..\\components\\error.vue'
export { default as Footer } from '../..\\components\\footer.vue'
export { default as Leaflet } from '../..\\components\\leaflet.vue'
export { default as LineChart } from '../..\\components\\lineChart.vue'
export { default as LineChartMontantParSecteur } from '../..\\components\\lineChartMontantParSecteur.vue'
export { default as LineChartMontantParSecteurParBailleur } from '../..\\components\\lineChartMontantParSecteurParBailleur.vue'
export { default as LineChartMontantParSecteurParRegion } from '../..\\components\\lineChartMontantParSecteurParRegion.vue'
export { default as ListeMenu } from '../..\\components\\listeMenu.vue'
export { default as MenuNavbar } from '../..\\components\\menuNavbar.vue'
export { default as MenuSide } from '../..\\components\\menuSide.vue'
export { default as SelectRegions } from '../..\\components\\selectRegions.vue'
export { default as TabActiviteProjet } from '../..\\components\\tabActiviteProjet.vue'
export { default as TabBailleurContent } from '../..\\components\\tabBailleurContent.vue'
export { default as TabBailleurListeProjet } from '../..\\components\\tabBailleurListeProjet.vue'
export { default as TabDecaissementProjet } from '../..\\components\\tabDecaissementProjet.vue'
export { default as TabIndicateurProjet } from '../..\\components\\tabIndicateurProjet.vue'
export { default as TabInfoProjet } from '../..\\components\\tabInfoProjet.vue'
export { default as TabRegionContent } from '../..\\components\\tabRegionContent.vue'
export { default as TabRegionListeProjet } from '../..\\components\\tabRegionListeProjet.vue'
export { default as TabsDetailProjet } from '../..\\components\\tabsDetailProjet.vue'
export { default as Title } from '../..\\components\\title.vue'

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
