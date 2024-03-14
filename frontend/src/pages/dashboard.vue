<script setup>
import ScrapperForm from '@/views/pages/scrapper-forms/ScrapperForm.vue'
import Models from '@/views/pages/tables/Models.vue'

// 👉 Images
import chart from '@images/cards/chart-success.png'
import paypal from '@images/cards/paypal-error.png'
import wallet from '@images/cards/wallet-info.png'
import axios from 'axios'


const nbDevicesWithPrice = ref(null);
const averagePhonePrice = ref(null);
const mostExpensivePhone = ref(null);

const fetchManufacturers = async () => {
  try {
    const response = await axios.get('http://127.0.0.1:8000/api/devices/');
    const devicesWithData = response.data.filter(device => device.last_price !== null);

    // Calculate the number of devices with a price
    nbDevicesWithPrice.value = devicesWithData.length;
    // Calculate the average price of devices with a price
    const totalPrices = devicesWithData.reduce((total, device) => total + device.last_price, 0);
    mostExpensivePhone.value = devicesWithData.reduce((max, device) => max.last_price > device.last_price ? max : device).model_name;
    console.log(mostExpensivePhone.value);
    averagePhonePrice.value = totalPrices / nbDevicesWithPrice.value;
    
    //Round to one decimal place
    averagePhonePrice.value = averagePhonePrice.value.toFixed(1);
    averagePhonePrice.value = `$${averagePhonePrice.value}`;
    nbDevicesWithPrice.value = `${nbDevicesWithPrice.value} Devices`;
  } catch (error) {
    console.error(error);
  }
};

fetchManufacturers();

</script>

<template>

  <VRow>
    <!-- 👉 Ventes -->
    <VCol cols="12" md="4">
      <CardStatisticsVertical v-bind="{
        title: 'Produits avec prix',
        image: wallet,
        stats: nbDevicesWithPrice,
        change: nbDevicesWithPrice
      }" />
    </VCol>
    <!-- 👉 Profits -->
    <VCol cols="12" md="4">
      <CardStatisticsVertical v-bind="{
        title: 'Average Phone Price',
        image: chart,
        stats: averagePhonePrice,
        change: 72.80,
      }" />
    </VCol><!-- 👉 Paiements -->
    <VCol cols="12" sm="4">
      <CardStatisticsVertical v-bind="{
        title: 'Téléphone le plus cher',
        image: paypal,
        stats: mostExpensivePhone,
        change: -14.82,
      }" />
    </VCol>
  </VRow>
  <VRow>
    <VCol cols="12">
      <VCard title="Modèles">
        <Models />
      </VCard>
    </VCol>
  </VRow>
  <VRow>
  </VRow>
</template>
