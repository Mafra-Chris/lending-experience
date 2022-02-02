<template>
  <div class="proposal-card">
    <div class="card-info">
      <h1 class="card-title">Proposta {{ proposalIndex }}</h1>
      <div>
        <h3 class="amount-subtitle">Valor disponibilizado</h3>
        <h2 class="amount-title">${{ offerAmount }}</h2>
      </div>
      <div>{{ interestRate }}% de juros ao mês</div>
      <el-row>
        <el-button type="text" @click="removeInstallment()">-</el-button>
        <span>{{ installments }}</span>
        <el-button type="text" @click="addInstallment()">+</el-button>
      </el-row>
      <div>{{ installmentValue }}</div>
      <div>{{ roundNumber(installmentValue * installments) }}</div>
    </div>
    <div class="accept-container">
      <el-button class="btn-accept" type="primary" round
        >Aceitar Proposta</el-button
      >
    </div>
  </div>
</template>

<script lang="ts">
import Vue from 'vue';

export default Vue.extend({
  name: 'ProposalCard',
  props: {
    offerAmount: Number,
    interestRate: Number,
    proposalIndex: Number,
  },
  data() {
    return {
      installments: 1,
    };
  },
  computed: {
    installmentValue(): number {
      let value =
        (this.interestRate / 100) * this.offerAmount +
        this.offerAmount / this.installments;

      return this.roundNumber(value);
    },
  },
  methods: {
    addInstallment() {
      if (this.installments < 12) this.installments++;
    },
    removeInstallment() {
      if (this.installments > 1) this.installments--;
    },
    roundNumber(number: number) {
      return Math.round(number * 1e2) / 1e2;
    },
  },
});
</script>
<style scoped>
.proposal-card {
  background-color: #212842;
  box-shadow: 0 20px 25px -5px rgb(0 0 0 / 0.1),
    0 8px 10px -6px rgb(0 0 0 / 0.1);
  color: white;
  width: 300px;
  padding: 3rem 1rem 3rem 1rem;
  text-align: left;
}
.accept-container {
  text-align: center;
  margin-top: 1.5rem;
}

.card-info {
  padding: 0 4rem 0 4rem;
  text-align: left;
}

.btn-accept {
  width: 85%;
}

.card-title {
  margin: 0;
  font-size: 1.4rem;
  font-weight: 500;
  margin-bottom: 1rem;
}

.amount-title {
  margin: 0 0 1.5rem 0;
  font-size: 1.4;
  font-weight: 500;
}

.amount-subtitle {
  margin: 0rem;
  font-size: 0.9rem;
  font-weight: 300;
  color: #b3b5bc;
}
</style>
