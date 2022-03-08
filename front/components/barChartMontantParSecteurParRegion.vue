<template>
  <BarChart :options="montantSecteur.options" :series="montantSecteur.series" />
</template>
<script>

import {mapState} from 'vuex'

export default {
  computed: {
    ...mapState('region', {
      montantSecteurParRegion: (state) => state.montantSecteurParRegion,
      secteurs: (state) => state.secteurs,
      montantSecteur: (state) => {
        let opt = JSON.parse(JSON.stringify(state.montantSecteurParRegion));
        const sects = state.secteurs;
        opt['series'].map(serie => {
          const val = sects.find(se => se.code == serie.name)
          serie.name = val.sector;
        })
        return opt;
      },
      errors: (state) => state.errors,
    }),
  },
}
</script>
