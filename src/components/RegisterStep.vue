<template>
  <div>
    <el-form
      :rules="rules"
      ref="signupForm"
      :model="signupForm"
      label-position="top"
    >
      <el-form-item label="Email" prop="email">
        <el-input v-model="email"></el-input>
      </el-form-item>
      <el-form-item label="Senha" prop="password">
        <el-input
          v-model="password"
          show-password
          placeholder="Mínimo 8 caracteres"
        ></el-input>
      </el-form-item>
      <el-form-item prop="termsChecked">
        <el-checkbox v-model="termsChecked"
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
      password: '',
      rules: {
        isTermsChecked: [
          {
            required: true,
            message: 'É obrigatório aceitar os termos.',
            trigger: 'blur',
          },
        ],
        password: [
          {
            required: true,
            message: 'Insira uma senha válida.',
            trigger: 'blur',
          },
        ],
        email: [
          {
            required: true,
            message: 'Insira uma email válido.',
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
        this.$store.commit('setEmail', { email: value });
      },
    },
    isTermsChecked: {
      get() {
        return this.$store.state.signup.isTermsChecked;
      },
      set(value: boolean) {
        this.$store.commit('setIsTermsChecked', { isTermsChecked: value });
      },
    },
    signupForm(): object {
      return {
        email: this.email,
        isTermsChecked: this.isTermsChecked,
        password: this.password,
      };
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
