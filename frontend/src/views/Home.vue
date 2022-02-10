<template>
  <div>
    <ErrorDialog
      :message="errorMessage.message"
      :status="errorMessage.status"
      :isDialogVisible="isError"
    />

    <Navbar />
    <div class="main" v-if="isLoaded">
      <div class="main-title">
        <h1>Parabéns, {{ companyName }}</h1>
        <h2 class="main-subtitle">
          Agora você está mais perto de chegar ao próximo nível!
        </h2>
      </div>
      <el-row>
        <el-col :sm="12" class="chosen-offer">
          <ProposalCard
            :interestRate="chosenOffer.interest"
            :monthlyRevenue="monthlyRevenue"
            :amountPerc="chosenOffer.amountPerc"
            :isChosen="true"
            :installmentsChosen="installments"
            :taxValue="chosenOffer.taxValue"
          />
        </el-col>
        <el-col :xs="24" :sm="12" class="hidden-xs-only banknote-col">
          <img class="money-img" src="@/assets/banknote-animate.svg" alt="" />
        </el-col>
      </el-row>
    </div>

    <div v-if="isError">
      <img style="height: 90vh" src="@/assets/No-data-rafiki.svg" alt="" />
    </div>
    <Footer />
  </div>
</template>

<script lang="ts">
import Vue from 'vue';
import Navbar from '../components/Navbar.vue';
import ProposalCard from '../components/ProposalCard.vue';
import Footer from '../components/Footer.vue';
import ErrorDialog from '../components/ErrorDialog.vue';
import axios, { AxiosResponse } from 'axios';
import 'element-ui/lib/theme-chalk/display.css';
import { Offer } from '../types/offer';
import { ErrorMessage } from '../types/error';
import { AtomSpinner } from 'epic-spinners';

export default Vue.extend({
  name: 'Home',
  components: { Navbar, ProposalCard, Footer, ErrorDialog, AtomSpinner },
  data() {
    return {
      companyName: '',
      monthlyRevenue: 0,
      chosenOffer: {} as Offer,
      offerId: 0,
      installments: 0,
      isLoaded: false,
      isError: false,
      errorMessage: {
        message: '',
        status: 0,
      } as ErrorMessage,
    };
  },
  mounted: async function () {
    let flag = true;

    await axios
      .get(`api/company-detail/${this.$store.state.user.idCompany}/`)
      .then(async (response: AxiosResponse) => {
        this.monthlyRevenue = response.data.monthly_revenue;
        this.offerId = response.data.chosen_offer;
        this.installments = response.data.installments;
        this.companyName = response.data.name;
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
        .get(`api/offer-detail/${this.offerId}/`)
        .then(async (response: AxiosResponse) => {
          console.log(response.data);
          this.chosenOffer = {
            type: response.data.type,
            amountPerc: response.data.amount_perc,
            interest: response.data.interest,
            taxValue: response.data.tax_value,
            id: response.data.id_offer,
          };
          console.log(this.chosenOffer);
          this.isLoaded = true;
        })
        .catch((error) => {
          flag = false;
          this.errorMessage = {
            message: 'Erro ao buscar proposta escolhida.',
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
.money-img {
  width: 100%;
  float: left;
  filter: hue-rotate(4deg) brightness(1.2);
}

@media (min-width: 1024px) {
  .money-img {
    width: 80%;
    float: left;
    filter: hue-rotate(4deg) brightness(1.2);
  }
}
.main {
  margin-top: 3rem;
}
.main-title {
  margin-bottom: 2rem;
}
.main-subtitle {
  color: #bbbabf;
  font-weight: 300;
}
.chosen-offer {
  display: flex;
  justify-content: center;
}
</style>
