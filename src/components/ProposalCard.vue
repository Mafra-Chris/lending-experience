<template>
  <div class="proposal-card">
    <div class="card-info">
      <h1 class="card-title">
        Proposta {{ isChosen ? 'Escolhida' : proposalIndex }}
      </h1>

      <div class="amount">
        <h3 class="subtitle">Valor disponibilizado</h3>
        <h2 class="amount-title">
          {{
            offerAmount.toLocaleString('en-US', {
              style: 'currency',
              currency: 'USD',
            })
          }}
        </h2>
      </div>

      <div>
        <ul class="topics">
          <li>
            <font-awesome-icon
              icon="chevron-circle-right"
              class="topics-icon"
            />
            Receba em até 7 dias úteis.
          </li>
          <li>
            <font-awesome-icon
              icon="chevron-circle-right"
              class="topics-icon"
            />
            Pagamento será realizado via boleto.
          </li>
          <li>
            <font-awesome-icon
              icon="chevron-circle-right"
              class="topics-icon"
            />
            {{ interestRate }}% de juros ao mês.
          </li>
        </ul>
      </div>

      <div class="installments">
        <h2 v-if="isChosen" class="subtitle">Quantidade de parcelas</h2>
        <h2 v-else class="card-title">Em quantas parcelas?</h2>
        <h3 v-if="isChosen" class="amount-title">{{ installmentsChosen }}</h3>
        <div v-else>
          <el-button
            type="text"
            class="installment-button"
            @click="removeInstallment()"
            ><font-awesome-icon icon="minus" size="lg"
          /></el-button>
          <span class="installments-count">{{ installments }}</span>
          <el-button
            type="text"
            class="installment-button"
            @click="addInstallment()"
            ><font-awesome-icon icon="plus" size="lg"
          /></el-button>
        </div>
      </div>

      <div>
        <span class="subtitle">Taxa</span>
        <h2 class="amount-title">
          {{
            taxValue.toLocaleString('en-US', {
              style: 'currency',
              currency: 'USD',
            })
          }}
        </h2>
      </div>
      <div class="installment-value">
        <span class="subtitle">Valor de cada parcela</span>
        <h2 class="amount-title">
          {{
            installmentValue.toLocaleString('en-US', {
              style: 'currency',
              currency: 'USD',
            })
          }}
        </h2>
      </div>
    </div>
    <div v-if="!isChosen" class="accept-container">
      <el-button class="btn-accept" type="primary" round @click="chooseOffer()"
        >Aceitar Proposta</el-button
      >
    </div>
  </div>
</template>

<script lang="ts">
import router from '@/router';
import Vue from 'vue';

export default Vue.extend({
  name: 'ProposalCard',
  props: {
    interestRate: { type: Number, required: true },
    proposalIndex: { type: Number },
    monthlyRevenue: { type: Number, required: true },
    amountPerc: { type: Number, required: true },
    isChosen: { type: Boolean, required: true },
    taxValue: { type: Number, required: true },
    installmentsChosen: { type: Number },
    offerId: { type: Number },
  },
  data() {
    return {
      installments: 1,
    };
  },
  computed: {
    offerAmount(): number {
      return this.monthlyRevenue * (this.amountPerc / 100);
    },
    installmentValue(): number {
      let value =
        (this.interestRate / 100) * this.offerAmount +
        this.offerAmount / this.installments;

      return this.round2Decimals(value);
    },
    installmentsMax(): number {
      if (this.monthlyRevenue <= 10000) {
        return 6;
      } else if (this.monthlyRevenue > 10000) {
        return 12;
      }
      return 0;
    },
  },
  methods: {
    addInstallment() {
      if (this.installments < this.installmentsMax) this.installments++;
    },
    removeInstallment() {
      if (this.installments > 1) this.installments--;
    },
    round2Decimals(number: number) {
      return Math.round(number * 1e2) / 1e2;
    },
    chooseOffer() {
      this.$store.commit('setOffer', {
        offer: { id: this.offerId, installments: this.installments },
      });
      router.push('/');
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
  max-width: 285px;
  padding: 3rem 1rem 3rem 1rem;
  text-align: left;
}
.accept-container {
  text-align: center;
  margin-top: 1.5rem;
}

.card-info {
  padding: 0 3rem 0 3rem;
  text-align: left;
}

.card-info > div {
  margin-top: 1.4rem;
}

.btn-accept {
  width: 90%;
}

.card-title {
  margin: 0;
  font-size: 1.4rem;
  font-weight: 500;
}

.amount-title {
  margin: 0;
  font-size: 1.8rem;
  font-weight: 500;
}

.subtitle {
  margin: 0rem;
  font-size: 0.9rem;
  font-weight: 300;
  color: #bbbabf;
  display: block;
}

.topics {
  list-style: none;
  padding: 0;
  font-weight: 300;
}

.topics li:not(:first-child) {
  margin-top: 0.3rem;
}

.topics-icon {
  margin-right: 0.25rem;
}
.installment-button {
  padding: 0;
}

.installments-count {
  margin: 0 0.5rem 0 0.5rem;
}
</style>
