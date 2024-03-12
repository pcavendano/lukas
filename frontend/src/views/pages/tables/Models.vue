<script setup>
import axios from 'axios';
import { ref } from 'vue';

const models = ref([]);
const currentPage = ref(1);
const totalPages = ref(1);

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
  if (currentPage.value < totalPages.value) {  // Corrected variable access
    currentPage.value++;
    fetchModels();
  }
};

const prevPage = () => {
  if (currentPage.value > 1) {  // Corrected variable access
    currentPage.value--;
    fetchModels();
  }
};

fetchModels();  // Fetch models initially
</script>

<template>
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
          Dernier Prix
        </th>
        <th>
          IMAGE
        </th>
      </tr>
    </thead>

    <tbody>
      <tr v-for="item in models" :key="item.model">
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
          {{ item.description }}
        </td>
        <td class="text-center">
          <img :src="`${item.image}`" :alt="item.name" width="50" height="50">
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
