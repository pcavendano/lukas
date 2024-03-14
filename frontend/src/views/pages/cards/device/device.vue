<template>
  <VRow>
    <VCol cols="8">
      <VCard class="justify-space-between py-8">
        <div class="d-flex justify-space-between flex-wrap flex-md-nowrap flex-column flex-md-row">
          <div class="mb-auto pa-5">
            <VImg aspect-ratio="16/9" :src="models.image" />
          </div>

          <VDivider :vertical="$vuetify.display.mdAndUp" />

          <div>
            <VCardItem>
              <VCardTitle class="text-h4 ">{{ models.model_name }}</VCardTitle>
            </VCardItem>

            <VCardText>
              Smartphone {{ models.model_name }}. Annoncé en septembre 2019. Caractéristiques : écran 5,8 pouces,
              processeur Apple A13 Bionic
            </VCardText>

            <VCardText class="text-subtitle-1">
              <span>Prix d'achat maximal proposé :</span> <span class="font-weight-medium">
                <!-- si le prix est null, afficher N/A -->
                {{ models.last_price ? `$${models.last_price}` : 'N/A' }}
              </span>
            </VCardText>
            <VCardText class="text-subtitle-1">
              <span>Marge de profit suggérée :</span> <span class="font-weight-medium">
                <!-- si le prix est null, afficher N/A -->
                {{ models.last_price ? `${profitPercentage * 100}%` : 'N/A' }}
              </span>
            </VCardText>
            <v-list class="ml-2 word-count" lines="three" select-strategy="classic">
              <v-list-subheader>Général</v-list-subheader>
              <!-- For each element in checkboxes variable create a v-list-item -->
              <v-list-item v-for="checkbox in checkboxes" :key="checkbox.value" :value="checkbox.value">
                <template v-slot:prepend="{ isActive }">
                  <v-list-item-action start>
                    <v-checkbox-btn :model-value="isActive" @click="toggleCheckbox(checkbox)"></v-checkbox-btn>
                  </v-list-item-action>
                </template>
                <v-list-item-title>{{ checkbox.label }}</v-list-item-title>
                <v-list-item-subtitle>{{ checkbox.text }}</v-list-item-subtitle>
              </v-list-item>
            </v-list>
          </div>
        </div>
      </VCard>
    </VCol>
    <VCol cols="4" order="2" order-lg="2" class="member-pricing-bg">
      <div class="membership-pricing d-flex flex-column align-left py-14">
        <!-- i want to display h1 at the top of the card -->
        <VCardTitle class="text-h4 text-left">Votre profit serait de<br> <sub class="text-h4" style="color: green">{{
              (models.last_price * profitPercentage) }}CAD</sub>
        </VCardTitle>
        <div class="ml-6">
          <div class="pt-12">
            <h2 class="text-h5">Prix suggéré de rachat</h2>
            <p class="mb-5">
              <sub class="text-h5" style="color: green">${{ models.last_price }}</sub>
              <sub class="text-h5" style="color: green">CAD</sub>
            </p>
            <h2 class="text-h5">Prix suggéré de revente</h2>
            <p class="mb-5">
              <sub class="text-h5" style="color: green">${{ (models.last_price * (1 + profitPercentage)) }}</sub>
              <sub class="text-h5" style="color: green">CAD</sub>
            </p>
            <div :class="{ toShow: showDiscountedPrice, toHide: !showDiscountedPrice }">
              <h2 class="text-h5">Prix offert après réparations</h2>
              <p class="mb-5">
                <sub class="text-h5" style="color: green">{{ discountedPrice < 0 ? ' Recyclage 20$' : (discountedPrice
              + '$') }} </sub>
                    <sub class="text-h5" style="color: green">CAD</sub>
              </p>
            </div>
            <VBtn class="mt-8" @click="calculatePriceAfterRepair">
              Calculer votre prix d'achat
            </VBtn>
          </div>
        </div>
      </div>
    </VCol>
  </VRow>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import axios from 'axios';

const models = ref({});
const profitPercentage = 0.20;
const checkboxPrices = {
  alimentation: 287,
  verrouillage: 257,
  touchscreen: 175,
  glass: 175,
  others: 217
};

const checkboxes = [
  {
    value: 'alimentation',
    label: 'Alimentation',
    text: 'L\'appareil s\'allume-t-il et navigue-t-il correctement vers l\'écran d\'accueil ?',
    isActive: false
  },
  {
    value: 'verrouillage',
    label: 'Verrouillage',
    text: 'Le verrouillage d\'activation est-il désactivé ? (par exemple, Find My iPhone ou Reactivation Lock, Samsung\'s Reactivation Lock ou Android\'s Activation Lock)',
    isActive: false
  },
  {
    value: 'touchscreen',
    label: 'Écran tactile',
    text: 'L\'écran tactile est-il exempt de problèmes d\'affichage ? Exemple : pixels non fonctionnels, lignes bleues, scintillement',
    isActive: false
  },
  {
    value: 'glass',
    label: 'Vitre',
    text: 'L\'écran et/ou le verre arrière sont-ils exempts de fissures et d\'éclats ?',
    isActive: false
  },
  {
    value: 'others',
    label: 'Autres',
    text: 'Toutes les fonctions suivantes fonctionnent-elles correctement ? (caméras, haut-parleurs, bouton d\'accueil, bouton d\'alimentation, boutons de volume, microphone, batterie, charnière et port de charge)',
    isActive: false
  }
];

const discountedPrice = ref(null);
const showDiscountedPrice = ref(false);

const calculatePriceAfterRepair = () => {
  discountedPrice.value = models.value.last_price;
  let discountedPricein = models.value.last_price;
  const checkedCheckboxes = checkboxes.filter(cb => cb.isActive);
  let count = 0;
  checkedCheckboxes.forEach(checkbox => {
    const price = checkboxPrices[checkbox.value];
    discountedPricein -= price;
    count++;
  });
  if (count == 0) {
    discountedPrice.value = 0;
  } else {
    discountedPrice.value = discountedPricein;
  }
  showDiscountedPrice.value = true;
};

const fetchDevice = async () => {
  try {
    const id = useRouter().currentRoute.value.params.id;
    const url = `http://127.0.0.1:8000/api/models/${id}/`;
    const response = await axios.get(url);
    models.value = response.data;
  } catch (error) {
    console.error(error);
  }
};

const toggleCheckbox = (checkbox) => {
  checkbox.isActive = !checkbox.isActive;
};

fetchDevice();
</script>

<style lang="scss" scoped>
.avatar-center {
  position: absolute;
  border: 3px solid rgb(var(--v-theme-surface));
  inset-block-start: -2rem;
  inset-inline-start: 1rem;
}

// membership pricing
.member-pricing-bg {
  position: relative;
  background-color: rgba(var(--v-theme-on-surface), var(--v-hover-opacity));
}

.membership-pricing {
  sup {
    inset-block-start: 9px;
  }
}

.toShow {
  display: block;
}

.toHide {
  display: none;
}

</style>
