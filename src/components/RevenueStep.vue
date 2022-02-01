<template>
  <div>
    <el-form
      :rules="rules"
      ref="signupForm"
      :model="signupForm"
      label-position="top"
    >
      <el-form-item label="Receita média mensal" prop="monthlyRevenue">
        <el-input v-model="signupForm.monthlyRevenue"></el-input>
        <div class="revenue-slider-label">
          <span>0</span><span>2 milhões</span>
        </div>
        <div class="revenue-slider">
          <el-slider
            v-model="signupForm.monthlyRevenue"
            :min="0"
            :max="2000000"
          >
          </el-slider>
        </div>
      </el-form-item>
      <el-form-item
        label="Como você planeja usar esse crédito?"
        prop="moneyPurpose"
      >
        <el-select
          v-model="signupForm.moneyPurpose"
          placeholder="Escolha o propósito"
        >
          <el-option
            v-for="item in purposeOptions"
            :key="item.value"
            :label="item.label"
            :value="item.value"
          >
          </el-option>
        </el-select>
      </el-form-item>
      <div class="">
        <el-form-item>
          <el-button type="info" @click="previousStep()" class="btn-next"
            >Voltar</el-button
          >
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="nextStep()" class="btn-next"
            >Avançar</el-button
          >
        </el-form-item>
      </div>
    </el-form>
  </div>
</template>

<script lang="ts">
import Vue from 'vue';
export default Vue.extend({
  name: 'Signup',
  data() {
    return {
      signupForm: {
        name: '',
        cnpj: '',
        website: '',
        segmentOption: '',
        monthlyRevenue: 0,
        moneyPurpose: '',
        termsChecked: false,
      },
      rules: {
        name: [
          {
            required: true,
            message: 'Insira o nome da empresa.',
            trigger: 'blur',
          },
        ],
      },
      purposeOptions: [
        {
          value: 'mkt',
          label: 'Marketing Digital',
        },
        {
          value: 'debt',
          label: 'Re-pagamento de dívida',
        },
        {
          value: 'workingCapital',
          label: 'Capital de giro',
        },
        {
          value: 'others',
          label: 'Outros',
        },
      ],
    };
  },
  computed: {
    monthlyRevenue: {
      get() {
        return this.$store.state.signup.monthlyRevenue;
      },
      set(value: string) {
        this.$store.commit('setMonthlyRevenue', value);
      },
    },
    moneyPurpose: {
      get() {
        return this.$store.state.signup.moneyPurpose;
      },
      set(value: string) {
        this.$store.commit('setMoneyPurpose', value);
      },
    },
  },
  methods: {
    nextStep() {
      this.$store.commit('incrementCurrentStep');
    },
    previousStep() {
      this.$store.commit('decrementCurrentStep');
    },
  },
});
</script>

<style scoped>
.revenue-slider-label {
  color: #8c8c8c;
  font-size: 12px;
  display: flex;
  justify-content: space-between;
  margin-bottom: -18px;
}
.revenue-slider {
  padding: 0 0.4rem 0 0.4rem;
}
</style>
