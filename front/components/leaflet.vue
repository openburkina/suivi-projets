<template>
    <div style="height: 80vh ;" class="mt-5">
        <client-only>
            <l-map class="map" :zoom=3 :center=centerPoint>
                <l-tile-layer url="http://{s}.tile.osm.org/{z}/{x}/{y}.png"></l-tile-layer>
                <l-polygon 
                v-for="d in regions" 
                :lat-lngs="d.boundary.coordinates" 
                :weight="0.5" color="#000" 
                :fillColor="getRegionColor(d.country)"
                 :fillOpacity="1" 
                 @mouseenter="hovering(d.region)" 
                 @mouseleave="notHovering(d.region)" 
                 :ref="d.region" :key="d.id">
                        <l-popup ref="popup">
                           <p>{{ normalizeString(d.region) }}</p>
                            <v-card >
                                <template>
                                    <v-simple-table>
                                        <template v-slot:default>
                                        <tbody>
                                            <tr>
                                                <td>Montant</td>
                                                <td>{{ getRegionValue(d.country) }}</td>
                                            </tr>
                                        </tbody>
                                        </template>
                                    </v-simple-table>
                                    </template>
                            </v-card>
                        </l-popup>
                </l-polygon>
                <l-control position="bottomright">
                    <div class="info legend">
                        <div v-for="interval in colorIntervals.slice().reverse()" :key="interval.key">
                            <i :style="'background:'+interval.color"></i>
                            {{ interval.value }} 
                            <br>
                        </div>
                    </div>
                </l-control>
            </l-map>
        </client-only>
    </div>
</template>
<script>
import * as regions from '../static/data/regions_cached.json';
import { mapState } from 'vuex'

export default {
  data() {
    return {
      centerPoint : [-3.993859, 29.371619],
      colorIntervals: [
                {
                    "key": 0,
                    "value": "0",
                    "color": "#FFF"
                },
                {
                    "key": 1,
                    "value": "< 100.000",
                    "color": "#dcfce7"
                },
                {
                    "key": 2,
                    "value": "< 1.000.000",
                    "color": "#86efac"
                },
                {
                    "key": 3,
                    "value": "> 1.000.000",
                    "color": "#22c55e"
                },
            ],
            
            regions: regions.data,
    }
  },

  methods: {
     normalizeString(string) {
            let normalized = string.toLowerCase();
            return normalized.charAt(0).toUpperCase() + normalized.slice(1);
        },
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
    
     getRegionColor(title) {
            try {
                let region = this.leafletData.find((region) => region.title == title);
                let color = "#86efac"
                if (region != undefined){
                    if (region.sum > 1000000000) color = "#22c55e"
                    else if (region.sum > 100000000) color = "#86efac"
                    else if (region.sum > 0) color = "#dcfce7"
                }
                return color
            } catch (e) {
                return "#FFF043"
            }
        },
        getRegionValue(title) {
            try {
                let region = this.leafletData.find((region) => region.title == title);
                if (region != undefined){
                    return this.formatValue(region.value)
                }
                return 0
            } catch (e) {
                return 0
            }
        },
        formatValue(amount, currency) {
            if (amount==null && currency==null){
                amount = 0
                currency = "$"
            }
            return (
                amount
                .toFixed(2) // always two decimal digits
                .replace('.', ',') // replace decimal point character with ,
                .replace(/(\d)(?=(\d{3})+(?!\d))/g, '$1.') + ' ' + currency
            ) 
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
.map{
    z-index:0;
}
.info {
    padding: 6px 8px;
    font: 14px/16px Arial, Helvetica, sans-serif;
    background: white;
    box-shadow: 0 0 15px rgba(0,0,0,0.2);
    border-radius: 5px;
}
.legend {
    line-height: 18px;
    color: #FFF;
}
.legend i {
    width: 18px;
    height: 18px;
    float: left;
    margin-right: 8px;
    background-color: #FFF;
}
</style>
