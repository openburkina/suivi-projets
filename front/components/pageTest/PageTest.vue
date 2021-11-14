<template>
    <v-app>
        <nav>
            <v-toolbar id="toolbar">
                <v-toolbar-title>
                    <span class="px-3">Title</span>
                </v-toolbar-title>
                <v-spacer></v-spacer>
                <v-btn color="primary" class="hidden-md-and-up" @click="toggleMenu = !toggleMenu">
                    <v-icon>mdi-menu</v-icon>
                </v-btn>
                <v-menu
                v-model="showMenu"
                :absolute="toggleMenu"
                :attach="'#toolbar'"
                :content-class="'px-2 elevation-0'"
                :nudge-top="$vuetify.breakpoint.smAndDown?-52:-12"
                min-width="100%">
                    <div class="d-flex flex-column flex-md-row justify-end">
                        <v-btn color="success" class="ma-1">text1</v-btn>
                        <v-btn color="success" class="ma-1">text1</v-btn>
                        <v-btn color="success" class="ma-1">text1</v-btn>
                        <v-btn color="success" class="ma-1">text1</v-btn>
                    </div>
                </v-menu>
            </v-toolbar>
        </nav>
    </v-app>
</template>

<script>
export default {
  data() {
        return {
            toggleMenu: false,
        }
    },
    computed: {
        showMenu() {
            return this.toggleMenu || this.$vuetify.breakpoint.mdAndUp
        }
    }
};
</script>
