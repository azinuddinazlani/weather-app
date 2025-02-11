<template>
  <v-app>
    <v-main>
      <Weather />
    </v-main>
  </v-app>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import Weather from "./components/Weather.vue"; // Import the Weather component

export default defineComponent({
  components: {
    Weather, // Register the Weather component
  },
});
</script>