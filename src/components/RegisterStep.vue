<template>
  <div>
    <el-form
      :rules="rules"
      ref="signupForm"
      :model="signupForm"
      label-position="top"
    >
      <el-form-item label="Email" prop="email">
        <el-input v-model="signupForm.email"></el-input>
      </el-form-item>
      <el-form-item label="Senha" prop="password">
        <el-input
          v-model="signupForm.password"
          show-password
          placeholder="Mínimo 8 caracteres"
        ></el-input>
      </el-form-item>
      <el-form-item prop="termsChecked">
        <el-checkbox v-model="signupForm.termsChecked"
          >Li e concordo com os Termos de Uso.</el-checkbox
        >
      </el-form-item>
      <div>
        <el-form-item>
          <el-button type="info" @click="previousStep()" class="btn-next"
            >Voltar</el-button
          >
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="finishForm()" class="btn-next"
            >Finalizar</el-button
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
      progressPerc: 0,
      currentStep: 0,
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
    };
  },
  computed: {
    email: {
      get() {
        return this.$store.state.signup.email;
      },
      set(value: string) {
        this.$store.commit('setEmail', value);
      },
    },
    isTermsChecked: {
      get() {
        return this.$store.state.signup.isTermsChecked;
      },
      set(value: boolean) {
        this.$store.commit('setIsTermsChecked', value);
      },
    },
  },
  methods: {
    finishForm() {
      this.$store.commit('incrementCurrentStep');
    },
    previousStep() {
      this.$store.commit('decrementCurrentStep');
    },
  },
});
</script>
