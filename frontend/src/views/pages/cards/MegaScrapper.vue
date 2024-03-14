<script setup>
import avatar1 from '@images/avatars/avatar-1.png'
import avatar2 from '@images/avatars/avatar-2.png'
import avatar3 from '@images/avatars/avatar-3.png'
import avatar4 from '@images/avatars/avatar-4.png'
import eCommerce2 from '@images/eCommerce/2.png'
import axios from 'axios';
const isCardDetailsVisible = ref(false)
const success = ref(null)
const toggleCardDetails = () => {
    isCardDetailsVisible.value = !isCardDetailsVisible.value
}



const firstScrapper = async () => {
    try {
        const response = await axios.get('http://127.0.0.1:8000/api/scrapper/first-scrapper');
        console.log(response.data);
        success.value = response.data;
        return response.data;
    } catch (error) {
        console.error(error);
    }
}
</script>

<template>
    <VRow>

        <!-- 👉 Apple iPhone 11 Pro -->
        <VCol sm="6" cols="12" style="display: none;">
            <VCard>
                <div class="d-flex justify-space-between flex-wrap flex-md-nowrap flex-column flex-md-row ">
                    <div class="ma-auto pa-5">
                        <VImg width="137" height="176" :src="eCommerce2" />
                    </div>

                    <VDivider :vertical="$vuetify.display.mdAndUp" />

                    <div>
                        <VCardItem>
                            <VCardTitle>Apple iPhone 11 Pro</VCardTitle>
                        </VCardItem>

                        <VCardText>
                            Apple iPhone 11 Pro smartphone. Announced Sep 2019. Features 5.8″ display Apple A13 Bionic
                        </VCardText>

                        <VCardText class="text-subtitle-1">
                            <span>Price :</span> <span class="font-weight-medium">$899</span>
                        </VCardText>

                        <VCardActions class="justify-space-between">
                            <VBtn>
                                <VIcon icon="bx-cart-add" />
                                <span class="ms-2">Add to cart</span>
                            </VBtn>

                            <VBtn color="secondary" icon="bx-share-alt" />
                        </VCardActions>
                    </div>
                </div>
            </VCard>
        </VCol>
        <!-- 👉 Support -->
        <VCol cols="12" md="12" lg="12">
            <VCard class="text-center">
                <VCardText class="d-flex flex-column justify-center align-center">

                    <h6 class="text-h6">
                        Premier Scraper
                    </h6>
                </VCardText>

                <VCardText>
                    <p>
                        Ce bouton déclenche le premier scraper pour récupérer la liste des fabricants, permettant
                        ensuite la récupération des modèles pour chaque fabricant.
                    </p>
                </VCardText>
                <VCardText>
                    <VBtn variant="elevated" class="spin-on-hover" :class="{ 'spin-on-hover': loading }" @click="firstScrapper" :disabled="loading">
                        <VIcon size="2rem" icon="bxs-invader" class="icon" />
                    </VBtn>
                </VCardText>
                <!-- Hidden text that displays when response.data is true nabd -->
                <VCardText v-if="success">
                    <p>
                        Le premier scraper a été déclenché avec succès.
                    </p>
                </VCardText>
                
            </VCard>
        </VCol>
    </VRow>
</template>

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

/* Define animation */
@keyframes spin {
    0% {
        transform: rotate(0deg);
    }

    100% {
        transform: rotate(360deg);
    }
}

/* Apply animation on hover */
.spin-on-hover:hover .icon {
    animation: spin 1s linear infinite;
}
</style>
