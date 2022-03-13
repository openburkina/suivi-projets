<template>
  <div style="height: 80vh" class="mt-5">
    <client-only>
      <l-map
        :zoom="5"
        :center="[9.548624660911141, 7.804160193482599]"
        class="map"
      >
        <l-tile-layer
          url="http://{s}.tile.osm.org/{z}/{x}/{y}.png"
        ></l-tile-layer>
        <l-marker
          v-for="d in leafletData"
          :lat-lng="d.lat_long"
          @mouseenter="hovering(d.region)"
          @mouseleave="notHovering(d.region)"
          :ref="d.region"
          :key="d.region"
        >
          <l-popup ref="popup" style="width: 250px">
            <v-simple-table>
              <template v-slot:default>
                <tbody>
                  <tr>
                    <th>Pays</th>
                    <td>{{ d.title }}</td>
                  </tr>
                  <tr>
                    <th>Montant total des projets</th>
                    <td>{{ d.sum }}</td>
                  </tr>
                </tbody>
              </template>
            </v-simple-table>
          </l-popup>
        </l-marker>
      </l-map>
    </client-only>
  </div>
</template>
<script>
import { mapState } from 'vuex'

export default {
  data() {
    return {
      lat: [8.592724737747833, 16.074241050333463],
      open: null,
      mock: [
        {
          id: 0,
          name: 'tchad',
          projet: '2',
          dra: '🇹🇩',
          budget: '$45M',
          expense: '100XAF',
          lat: [8.592724737747833, 16.074241050333463],
        },
      ],
    }
  },

  methods: {
    hovering(name) {
      this.$nextTick(() => {
        this.$refs[name][0].mapObject.openPopup()
      })
    },
    notHovering(name) {
      this.$nextTick(() => {
        this.$refs[name][0].mapObject.closePopup()
      })
    },
  },

  computed: {
    ...mapState('region', {
      sumProjectByCountry: (state) => state.sumProjectByCountry,
      details: (state) => state.details,
      errors: (state) => state.errors,
      leafletData: (state) => {
        let projects = JSON.parse(JSON.stringify(state.sumProjectByCountry))
        const regions = state.details
        projects.map((project) => {
          const val = regions.find(
            (region) => region.region_code == project.region
          )
          project.title = val.name
          project.lat_long = [val.longitude, val.latitude]
        })
        return projects
      },
    }),
  },
}
</script>
<style scoop lang="scss">
.map {
  z-index: 0;
}
</style>
