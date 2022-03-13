<template>
<div>
    <LineChart :options="montantSecteur.options" :series="montantSecteur.series" />
</div>
</template>
<script>

import {mapState} from 'vuex'

export default {
  computed: {
    ...mapState('bailleur', {
      montantSecteurParBailleur: (state) => state.montantSecteurParBailleur,
      secteurs: (state) => state.secteurs,
      montantSecteur: (state) => {
        let opt = JSON.parse(JSON.stringify(state.montantSecteurParBailleur));
        const sects = state.secteurs;
        opt['series'].map(serie => {
          const val = sects.find(se => se.code == serie.name)
          serie.name = val.sector;
        })
        return opt;
      },
      errors: (state) => state.errors
    }),
  },
}
</script>
