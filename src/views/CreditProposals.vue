<template>
  <div>
    <h1 class="page-title">
      Escolha a proposta que melhor se adequa a sua empresa
    </h1>
    <ul id="v-for-object" class="proposal-cards">
      <li v-for="(offer, index) in biggerOffers" v-bind:key="index">
        <ProposalCard
          :interestRate="offer.interest"
          :proposalIndex="index + 1"
          :monthlyRevenue="monthlyRevenue"
          :amountPerc="offer.amountPerc"
          :offerId="offer.id"
        />
      </li>
    </ul>
  </div>
</template>

<script lang="ts">
import Vue from 'vue';
import ProposalCard from '@/components/ProposalCard.vue';
import axios, { AxiosResponse } from 'axios';
import { Offer } from '@/types/offer';
export default Vue.extend({
  name: 'CreditProposals',
  components: {
    ProposalCard,
  },
  data() {
    return {
      monthlyRevenue: 0,

      biggerOffers: [] as Offer[],
      lowerOffers: [] as Offer[],
    };
  },
  mounted: async function () {
    await axios
      .get('https://61fb29d587801d0017a2c40d.mockapi.io/userNormal')
      .then(async (response: AxiosResponse) => {
        this.monthlyRevenue = response.data.monthlyRevenue;
      });

    await axios
      .get('https://61fb29d587801d0017a2c40d.mockapi.io/offers')
      .then(async (response: AxiosResponse) => {
        response.data.forEach((offer: Offer) => {
          if (offer.type === 'bigger') {
            this.biggerOffers.push(offer);
          } else if (offer.type === 'lower') {
            this.lowerOffers.push(offer);
          }
        });
      });
  },
});
</script>

<style scoped>
.proposal-cards {
  display: flex;
  justify-content: center;
  gap: 1rem;
  list-style: none;
  margin-top: 1rem;
  padding: 0;
}
.page-title {
  margin-top: 2rem;
}
</style>
