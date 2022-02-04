<template>
  <div>
    <Navbar />
    <div class="main" v-if="isLoaded">
      <div class="main-title">
        <h1>Parabéns, a55</h1>
        <h2>Agora você pode chegar ao próximo nível!</h2>
      </div>
      <el-row>
        <el-col :sm="12" class="hidden-xs-only chosen-offer">
          <ProposalCard
            :interestRate="chosenOffer.interest"
            :monthlyRevenue="monthlyRevenue"
            :amountPerc="chosenOffer.amountPerc"
          />
        </el-col>
        <el-col :xs="24" :sm="12">
          <img class="money-img" src="@/assets/banknote-animate.svg" alt=""
        /></el-col>
      </el-row>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from 'vue';
import Navbar from '@/components/Navbar.vue';
import ProposalCard from '@/components/ProposalCard.vue';
import axios, { AxiosResponse } from 'axios';
import { Offer } from '@/types/offer';

export default Vue.extend({
  name: 'Home',
  components: { Navbar, ProposalCard },
  data() {
    return {
      monthlyRevenue: 0,
      chosenOffer: {} as Offer,
      isLoaded: false,
    };
  },
  created() {
    axios
      .get('https://61fb29d587801d0017a2c40d.mockapi.io/userNormal')
      .then(async (response: AxiosResponse) => {
        console.log(response);
        this.monthlyRevenue = response.data.monthlyRevenue;
      });
    axios
      .get('https://61fb29d587801d0017a2c40d.mockapi.io/offers/2')
      .then(async (response: AxiosResponse) => {
        this.isLoaded = true;
        this.chosenOffer = response.data;
      });
  },
});
</script>

<style scoped>
.money-img {
  width: 80%;
  float: left;
}
.main {
  margin-top: 3rem;
}
.main-title {
  margin-bottom: 2rem;
}
.chosen-offer {
  display: flex;
  justify-content: center;
}
</style>
