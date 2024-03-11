<template>
  <VForm @submit.prevent>
    <VRow>
      <VCol cols="12">
        <!-- Dropdown input for selecting models -->
        <VSelect v-model="selectedModel" :items="models" item-title="model_name" item-value="model_name"
          label="Select a Model">
          <template #prepend-inner>
          </template>
        </VSelect>
        <!-- Afficher les détails du modèle sélectionné -->
        <div v-if="selectedModel">
          <!-- console.log selectedModel    -->
          <h2>Détails du modèle sélectionné</h2>
          {{ console.log(selectedModelDetails) }}
          <p><strong>Nom :</strong> {{ selectedModelDetails.model_name }}</p>
          <p><strong>Code :</strong> {{ selectedModelDetails.model_code }}</p>
          <p><strong>Fabricant :</strong> {{ selectedModelDetails.manufacturer.manufacturer_name }}</p>
          <img :src="selectedModel.image" :alt="selectedModelDetails.model_name" width="50" height="50">
        </div>
      </VCol>
    </VRow>
    <VRow>
      <VCol cols="12">
        <VTextField prepend-inner-icon="bxs-invader" label="Site Web" placeholder="www.bell.ca" />
      </VCol>
    </VRow>
    <VRow>
      <VCol cols="12">
        <VBtn type="submit" class="me-2">
          Lancez la recherche
        </VBtn>
        <VBtn color="secondary" type="reset" variant="tonal">
          Recommencer
        </VBtn>
      </VCol>
    </VRow>
  </VForm>
</template>

<script setup>
import axios from 'axios';
import { ref } from 'vue';

const models = ref([]);
const selectedModel = ref(null);
const selectedModelDetails = ref(null); // To store details of selected model

// Fetch models data from the Django REST API
axios.get('http://127.0.0.1:8000/api/models/')
  .then(response => {
    // Map the array of objects to extract only the model_name property
    const modelNames = response.data.map(model => model.model_name);
    models.value = response.data;
    console.log('test');
    console.log(response.data);
    console.log(modelNames);
  })
  .catch(error => {
    console.error(error);
  });

// Watch for changes in selectedModel and update selectedModelDetails accordingly
watch(selectedModel, (newValue, oldValue) => {
  if (newValue) {
    const modelDetails = models.value.find(model => model.model_name === newValue);
    if (modelDetails) {
      selectedModelDetails.value = modelDetails;
    }
  } else {
    selectedModelDetails.value = null;
  }
});
</script>
