<template>
    <v-container>
      <v-row justify="center">
        <v-col cols="12" md="6">
          <v-card>
            <v-card-title>Weather App</v-card-title>
            <v-card-text>
              <v-text-field
                v-model="city"
                label="Enter City"
                variant="outlined"
                density="comfortable"
              ></v-text-field>
              <v-btn @click="fetchWeather" color="primary">Get Weather</v-btn>
            </v-card-text>
            <v-card-text v-if="weather">
              <v-list>
                <v-list-item>
                  <v-list-item-title>City:</v-list-item-title>
                  <v-list-item-subtitle>{{ weather.city }}</v-list-item-subtitle>
                </v-list-item>
                <v-list-item>
                  <v-list-item-title>Temperature:</v-list-item-title>
                  <v-list-item-subtitle>{{ weather.temperature }}°C</v-list-item-subtitle>
                </v-list-item>
                <v-list-item>
                  <v-list-item-title>Humidity:</v-list-item-title>
                  <v-list-item-subtitle>{{ weather.humidity }}%</v-list-item-subtitle>
                </v-list-item>
                <v-list-item>
                  <v-list-item-title>Description:</v-list-item-title>
                  <v-list-item-subtitle>{{ weather.description }}</v-list-item-subtitle>
                </v-list-item>
              </v-list>
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </template>
  
  <script lang="ts">
  import { defineComponent } from "vue";
  import axios from "axios";
  
  export default defineComponent({
    data() {
      return {
        city: "",
        weather: null as null | {
          city: string;
          temperature: number;
          humidity: number;
          description: string;
        },
      };
    },
    methods: {
      async fetchWeather() {
        try {
          const response = await axios.post("http://localhost:8000/weather/", {
            city: this.city,
          });
          this.weather = response.data;
        } catch (error) {
          alert("Failed to fetch weather data");
        }
      },
    },
  });
  </script>