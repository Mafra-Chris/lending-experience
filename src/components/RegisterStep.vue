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
      <el-form-item prop="isTermsChecked">
        <el-checkbox v-model="isTermsChecked"
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
    const verifyTerms = (rule: object, value: boolean, callback: Function) => {
      if (value === false) {
        return callback(new Error('É obrigatório aceitar os termos.'));
      }
      return callback();
    };
    return {
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
    // isTermsChecked: {
    //   get() {
    //     return this.$store.state.signup.isTermsChecked;
    //   },
    //   set(value: boolean) {
    //     console.log(value);
    //     this.$store.commit('setIsTermsChecked', { isTermsChecked: value });
    //   },
    // },
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
        (valid: boolean) => {
          if (valid) {
            this.$store.commit('setProgressPerc', { progressPerc: 100 });
            alert(this.$store.state.signup);
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
