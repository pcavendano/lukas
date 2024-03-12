<template>
  <VForm @submit.prevent="submitForm">
    <VRow>
      <VCol cols="12">
        <VRow no-gutters>
          <VCol cols="12" md="9">
            <!-- Dropdown input for selecting models -->
            <VSelect v-model="selectedManufacturer" :items="manufacturers" item-title="manufacturer_name" item-value="manufacturer_code"
              label="Sélectionnez un Manufacturer">
              <template #prepend-inner></template>
            </VSelect>
          </VCol>
        </VRow>
      </VCol>
      <VCol cols="12">
        <VRow no-gutters>
          <!-- Display details of the selected model -->
          <div v-if="selectedManufacturerDetails">
            <h2>Détails du manufacturer sélectionné</h2>
            <p><strong>Nom:</strong> {{ selectedManufacturerDetails.manufacturer_name }}</p>
            <p><strong>Code:</strong> {{ selectedManufacturerDetails.manufacturer_code }}</p>
          </div>
        </VRow>
      </VCol>

      <VCol cols="12">
        <VRow no-gutters>
          <VCol cols="12" md="9">
            <!-- Dropdown input for selecting models -->
            <VSelect v-model="selectedModel" :items="models" item-title="model_name" item-value="model_name"
              label="Sélectionnez un modèle">
              <template #prepend-inner></template>
            </VSelect>
          </VCol>
        </VRow>
      </VCol>

      <VCol cols="12">
        <VRow no-gutters>
          <!-- Display details of the selected model -->
          <div v-if="selectedModelDetails">
            <h2>Détails du modèle sélectionné</h2>
            <p><strong>Nom:</strong> {{ selectedModelDetails.model_name }}</p>
            <p><strong>Code:</strong> {{ selectedModelDetails.model_code }}</p>
            <p><strong>Fabricant:</strong> {{ selectedModelDetails.manufacturer.manufacturer_name }}</p>
            <img :src="selectedModelDetails.image" :alt="selectedModelDetails.model_name" width="50" height="50">
          </div>
        </VRow>
      </VCol>

      <VCol cols="12">
        <VRow no-gutters>
          <VCol cols="12" md="9">
            <VTextField prepend-inner-icon="bxs-invader" label="Site Web" placeholder="www.bell.ca" />
          </VCol>
        </VRow>
      </VCol>

      <!-- Submit and reset button -->
      <VCol offset-md="3" cols="12" md="9" class="d-flex gap-4">
        <VBtn color="secondary" variant="tonal" type="reset" @click="resetForm">Réinitialiser</VBtn>
        <VBtn type="submit">Soumettre</VBtn>
      </VCol>

      <VCol cols="12">
        <VRow no-gutters>
          <!-- Display success message -->
          <div v-if="success">
          <h2 style="color: green;">{{ success }}</h2>
          </div>
        </VRow>
      </VCol>
    </VRow>
  </VForm>
</template>

<script setup>
import axios from 'axios';
import { ref, watch } from 'vue';

const models = ref([]);
const manufacturers = ref([]);
const selectedModel = ref(null);
const selectedModelDetails = ref(null);
const selectedManufacturer = ref(null);
const selectedManufacturerDetails = ref(null);
const success = ref(null);

// Fetch models data from the Django REST API
axios.get('http://127.0.0.1:8000/api/devices/')
  .then(response => {
    models.value = response.data;
  })
  .catch(error => {
    console.error(error);
  });

// Fetch manufacturers data from the Django REST API
axios.get('http://127.0.0.1:8000/api/manufacturers/')
  .then(response => {
    console.log(response.data);
    manufacturers.value = response.data;
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

// Watch for changes in selectedManufacturer and update selectedManufacturerDetails accordingly
watch(selectedManufacturer, (newValue, oldValue) => {
  if (newValue) {
    const modelDetails = manufacturers.value.find(manufacturer => manufacturer.manufacturer_code === newValue);
    if (modelDetails) {
      selectedManufacturerDetails.value = modelDetails;
    }
  } else {
    selectedManufacturerDetails.value = null;
  }
});

// Function to handle form submission
const submitForm = () => {
  if (selectedModelDetails.value) {
    const url = `http://127.0.0.1:8000/api/scrappe/${selectedModelDetails.value.model_code}`;
    axios.get(url)
      .then(response => {
        console.log(response.data);
        success.value = "Succès ! Le prix de rachat maximum est de $" + response.data.buyback_price;
      })
      .catch(error => {
        console.error(error);
      });
  }
};

const updateManufacturers = () => {
  if (selectedModelDetails.value) {
    const url = `http://127.0.0.1:8000/api/updateManufacturers/`;
    axios.get(url)
      .then(response => {
        console.log(response.data);
        success.value = "Succès ! Manufacturers:" + response.data;
      })
      .catch(error => {
        console.error(error);
      });
  }
};

// Function to reset the form
const resetForm = () => {
  success.value = null;
};
</script>
