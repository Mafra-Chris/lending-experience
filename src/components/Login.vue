<template>
  <div>
    <div>
      <h1 class="login-title">Login</h1>
    </div>
    <el-form :rules="rules" ref="loginForm" :model="loginForm">
      <el-form-item label="Email" prop="email" ref="emaill">
        <el-input
          v-model="loginForm.email"
          placeholder="contato@email.com"
        ></el-input>
      </el-form-item>
      <el-form-item label="Senha" prop="password">
        <!-- <router-link to="/password-lost" class="password-lost"
          >Esqueceu a senha?</router-link
        > -->

        <el-input v-model="loginForm.password" show-password></el-input>
      </el-form-item>
      <el-form-item>
        <el-button
          type="primary"
          @click="submitForm('loginForm')"
          class="btn-login"
          >Entrar</el-button
        >
      </el-form-item>
    </el-form>
    <el-divider></el-divider>
    <router-link to="/signup" class="link-sign-up">
      Ainda não tem conta?
      <span class="brand-blue"> Cadastre-se agora</span>
    </router-link>
  </div>
</template>

<script lang="ts">
import Vue from 'vue';
export default Vue.extend({
  name: 'Login',
  data() {
    return {
      loginForm: {
        email: '',
        password: '',
      },
      rules: {
        email: [
          {
            required: true,
            message: 'Insira seu email.',
            trigger: 'blur',
          },
          {
            type: 'email',
            message: 'Insira um email válido',
            trigger: ['blur', 'change'],
          },
        ],
        password: [
          {
            required: true,
            message: 'Insira sua senha.',
            trigger: 'blur',
          },
        ],
      },
    };
  },
  methods: {
    submitForm(formName: string) {
      (this.$refs[formName] as HTMLFormElement).validate((valid: boolean) => {
        if (valid) {
          alert('submit!');
        } else {
          console.log('error submit!!');
          return false;
        }
      });
    },
  },
});
</script>

<style scoped>
.password-lost {
  float: right;
}
</style>
