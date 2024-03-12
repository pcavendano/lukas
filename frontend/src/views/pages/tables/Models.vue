<script setup>
import axios from 'axios';
import { ref, computed } from 'vue';


const models = ref([]);
const currentPage = ref(1);
const totalPages = ref(1);
const selectedManufacturer = ref(null); // Define selectedManufacturer here
const manufacturers = ref([]); // Define manufacturers array

const fetchModels = async () => {
  try {
    const response = await axios.get('http://127.0.0.1:8000/api/models/', {
      params: {
        page: currentPage.value
      }
    });
    models.value = response.data.data;
    totalPages.value = response.data.total_pages;
  } catch (error) {
    console.error(error);
  }
};

const nextPage = () => {
  if (currentPage.value < totalPages.value) {
    currentPage.value++;
    fetchModels();
  }
};

const prevPage = () => {
  if (currentPage.value > 1) {
    currentPage.value--;
    fetchModels();
  }
};

const updatePrice = async (modelCode, item) => {
  try {
    const response = await axios.get(`http://127.0.0.1:8000/api/scrappe/${modelCode}`);
    item.last_price = response.data.buyback_price; // Mettre à jour directement la propriété last_price de l'élément
  } catch (error) {
    console.error(error);
  }
};

const daysSince = (dateString) => {
  // Calculer la différence en millisecondes entre la date actuelle et la date fournie
  const diffMs = new Date() - new Date(dateString);
  // Convertir les millisecondes en jours
  const diffDays = Math.floor(diffMs / (1000 * 60 * 60 * 24));
  return diffDays;
};

const fetchManufacturers = async () => {
  try {
    const response = await axios.get('http://127.0.0.1:8000/api/manufacturers/');
    manufacturers.value = response.data; // Assuming the response data is an array of manufacturers
  } catch (error) {
    console.error(error);
  }
};

fetchManufacturers(); // Fetch manufacturers data


fetchModels();  // Récupérer les modèles initialement

const filteredModels = computed(() => {
  if (!selectedManufacturer.value) {
    return models.value;
  }
  return models.value.filter(model => model.manufacturer.manufacturer_code === selectedManufacturer.value);
});
</script>

<template>
  <VSelect v-model="selectedManufacturer" :items="manufacturers" item-title="manufacturer_name" item-value="manufacturer_code" label="Filter by Marque">
    <template #prepend-inner></template>
  </VSelect>
  <VTable height="auto" fixed-header>
    <thead>
      <tr>
        <th class="text-uppercase">
          NOM
        </th>
        <th>
          CODE
        </th>
        <th>
          Marque
        </th>
        <th>
          Dernière Mise à jour
        </th>
        <th>
          PRIX DE RACHAT MAXIMUM
        </th>
        <th>
          IMAGE
        </th>
        <th>
          Mettre à jour le prix
        </th>
      </tr>
    </thead>

    <tbody>
      <tr v-for="item in filteredModels" :key="item.model">
        <td>
          {{ item.model_name }}
        </td>
        <td class="text-center">
          {{ item.model_code }}
        </td>
        <td class="text-center">
          {{ item.manufacturer.manufacturer_name }}
        </td>
        <td class="text-center">
          Il y a {{ daysSince(item.updated) }} jours
        </td>
        <td class="text-center" style="color: orange;">
          {{
    item.last_price
      ? "$" + item.last_price
      : "N/A"
  }}
        </td>
        <td class="text-center">
          <img :src="`${item.image}`" :alt="item.name" width="50" height="50">
        </td>
        <td class="text-center">
          <VBtn color="primary" @click="updatePrice(item.model_code, item)">Mettre à jour</VBtn>
        </td>
      </tr>
    </tbody>
  </VTable>
  <div class="pagination d-flex justify-center align-center mx-4 my-4 py-4 px-4">
    <v-btn @click="prevPage" :disabled="currentPage === 1" color="primary">Previous</v-btn>
    <span class="mx-4">Page {{ currentPage }} of {{ totalPages }}</span>
    <v-btn @click="nextPage" :disabled="currentPage === totalPages" color="primary">Next</v-btn>
  </div>
</template>
