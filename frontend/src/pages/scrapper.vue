<script setup>
import MegaScrapper from '@/views/pages/cards/MegaScrapper.vue';
import ScrapperForm from '@/views/pages/scrapper-forms/ScrapperForm.vue'
</script>

<template>
  <div>
    <VRow>
      <VCol cols="12" md="6">
        <!-- 👉 Vertical Form with Icons -->
        <VCard title="Sélectionnez ce que vous voulez scraper ?">
          <VCardText>
            <ScrapperForm />
          </VCardText>
        </VCard>
      </VCol>
      <VCol cols="12" md="6">
        <!-- 👉 Vertical Form with Icons -->
        <VCard title="Mega Scrapper">
          <VCardText>
            <MegaScrapper />
          </VCardText>
        </VCard>
      </VCol>
    </VRow>
  </div>
</template>
