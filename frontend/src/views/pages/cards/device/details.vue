<script setup>


const isCardDetailsVisible = ref(false)
</script>

<template>
  <VRow>
    <!-- 👉 Lifetime Membership -->
    <VCol md="6" lg="8" cols="12">
      <VCard>
        <VRow no-gutters>
          <VCol cols="12" sm="8" md="12" lg="7" order="2" order-lg="1">
            <VCardItem>
              <VCardTitle>Lifetime Membership</VCardTitle>
            </VCardItem>

            <VCardText>
              Here, I focus on a range of items and features that we use in life without giving them a second thought
              such as Coca Cola, body muscles and holding ones own breath. Though, most of these notes are not
              fundamentally necessary, they are such that you can use them for a good laugh, at a drinks party or for
              picking up women or men.
            </VCardText>

            <VCardText>
              <VDivider />
            </VCardText>

            <VCardText class="d-flex justify-center">
              <div class="me-auto pe-4">
                <p class="d-flex align-center mb-6">
                  <VIcon color="primary" icon="bx-lock-open" />
                  <span class="ms-3">Full Access</span>
                </p>

                <p class="d-flex align-center mb-0">
                  <VIcon color="primary" icon="bx-user" />
                  <span class="ms-3">15 Members</span>
                </p>
              </div>

              <VDivider v-if="$vuetify.display.smAndUp" vertical inset />

              <div class="ms-auto ps-4">
                <p class="d-flex align-center mb-6">
                  <VIcon color="primary" icon="bx-star" />
                  <span class="ms-3">Access all Features</span>
                </p>

                <p class="d-flex align-center mb-0">
                  <VIcon color="primary" icon="bx-trending-up" />
                  <span class="ms-3">Lifetime Free Update</span>
                </p>
              </div>
            </VCardText>
          </VCol>
          <VCol cols="12" sm="4" md="12" lg="5" order="1" order-lg="2" class="member-pricing-bg text-center">
            <div class="membership-pricing d-flex flex-column align-center py-14 h-100 justify-center">
              <p class="mb-5">
                <sub class="text-h5">$</sub>
                <sup class="text-h2 font-weight-medium">899</sup>
                <sub class="text-h5">USD</sub>
              </p>

              <p class="text-sm">
                5 Tips For Offshore <br> Software Development
              </p>

              <VBtn class="mt-8">
                Contact Now
              </VBtn>
            </div>
          </VCol>
        </VRow>
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
</style>
