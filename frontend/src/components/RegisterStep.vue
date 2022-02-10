<template>
  <div>
    <ErrorDialog
      :message="errorMessage.message"
      :status="errorMessage.status"
      :isDialogVisible="isError"
    />
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
      <el-form-item prop="isTermsChecked">
        <el-checkbox v-model="isTermsChecked"
          >Li e concordo com os Termos de Uso.</el-checkbox
        >
      </el-form-item>
      <div class="btn-pages">
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
import router from '../router';
import Vue from 'vue';
import axios, { AxiosResponse } from 'axios';
import { ErrorMessage } from '../types/error';
import ErrorDialog from '../components/ErrorDialog.vue';
export default Vue.extend({
  name: 'Signup',
  components: { ErrorDialog },
  data() {
    const verifyTerms = (rule: object, value: boolean, callback: Function) => {
      if (value === false) {
        return callback(new Error('É obrigatório aceitar os termos.'));
      }
      return callback();
    };
    return {
      isError: false,
      errorMessage: { message: '', status: 0 } as ErrorMessage,
      password: '',
      isTermsChecked: false,
      rules: {
        isTermsChecked: [{ validator: verifyTerms, trigger: 'blur' }],
        password: [
          {
            required: true,
            message: 'Insira uma senha válida.',
            trigger: 'blur',
          },
          {
            min: 8,
            message: 'Senha deve ter no mínimo 8 caracteres.',
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
      (this.$refs['signupForm'] as HTMLFormElement).validate(
        async (valid: boolean) => {
          if (valid) {
            this.$store.commit('setProgressPerc', { progressPerc: 100 });

            await axios
              .post('/api/company-create/', {
                name: this.$store.state.signup.name,
                cnpj: this.$store.state.signup.cnpj,
                segment: this.$store.state.signup.segmentOption,
                website: this.$store.state.signup.website,
                monthly_revenue: this.$store.state.signup.monthlyRevenue,
                money_purpose: this.$store.state.signup.moneyPurpose,
                email: this.$store.state.signup.email,
                password: this.password,
                chosen_offer: null,
                installments: null,
              })
              .then(async (response: AxiosResponse) => {
                this.$store.commit('setIdCompany', {
                  idCompany: response.data.id_company,
                });
                router.push('/proposals');
              })
              .catch((error) => {
                this.errorMessage = {
                  message: 'Erro ao criar empresa.',
                  status: error.response.status,
                };
                this.isError = true;
              });
          } else {
            return false;
          }
        }
      );
    },
    previousStep() {
      this.$store.commit('decrementCurrentStep');
    },
  },
});
</script>
