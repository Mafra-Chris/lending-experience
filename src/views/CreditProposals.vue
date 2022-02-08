<template>
  <div class="proposals-page">
    <ErrorDialog
      :message="errorMessage.message"
      :status="errorMessage.status"
      :isDialogVisible="isError"
    />
    <Navbar />
    <div v-if="isLoaded" class="content">
      <section>
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
              :isChosen="false"
              :taxValue="offer.taxValue"
            />
          </li>
        </ul>
      </section>
    </div>
    <div v-if="isError">
      <img style="height: 90vh" src="@/assets/No-data-rafiki.svg" alt="" />
    </div>
    <Footer />
  </div>
</template>

<script lang="ts">
import Vue from 'vue';
import ProposalCard from '@/components/ProposalCard.vue';
import axios, { AxiosResponse } from 'axios';
import { Offer } from '@/types/offer';
import Navbar from '@/components/Navbar.vue';
import Footer from '@/components/Footer.vue';
import { ErrorMessage } from '@/types/error';
import ErrorDialog from '@/components/ErrorDialog.vue';
export default Vue.extend({
  name: 'CreditProposals',
  components: {
    ProposalCard,
    Navbar,
    Footer,
    ErrorDialog,
  },
  data() {
    return {
      monthlyRevenue: 0,
      biggerOffers: [] as Offer[],
      lowerOffers: [] as Offer[],
      isError: false,
      errorMessage: { message: '', status: 0 } as ErrorMessage,
      isLoaded: false,
    };
  },
  mounted: async function () {
    let flag = true;

    await axios
      .get('https://61fb29d587801d0017a2c40d.mockapi.io/userNormal')
      .then(async (response: AxiosResponse) => {
        this.monthlyRevenue = response.data.monthlyRevenue;
      })
      .catch((error) => {
        flag = false;
        this.errorMessage = {
          message: 'Erro ao buscar valor de receita mensal.',
          status: error.response.status,
        };
      });
    if (flag) {
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
          this.isLoaded = true;
        })
        .catch((error) => {
          flag = false;
          this.errorMessage = {
            message: 'Erro ao buscar propostas disponíveis.',
            status: error.response.status,
          };
        });
    }
    if (!flag) {
      this.isError = true;
    }
  },
});
</script>

<style scoped>
.proposal-cards {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 1rem;
  list-style: none;
  margin-top: 1rem;
  padding: 0;
}
.page-title {
  margin: 3rem 0 3rem 0;

  font-size: 2rem;
}

.proposals-page {
  height: 100%;
}

.content {
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>
