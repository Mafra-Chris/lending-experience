<template>
  <div>
    <el-form
      :rules="rules"
      ref="signupForm"
      :model="signupForm"
      label-position="top"
    >
      <el-form-item label="Nome" prop="name">
        <el-input v-model="signupForm.name"></el-input>
      </el-form-item>
      <el-form-item
        label="Para qual CNPJ deseja solicitar crédito?"
        prop="cnpj"
        placeholder="00.000.000/0000-00"
      >
        <el-input v-model="cnpj"></el-input>
      </el-form-item>
      <el-form-item label="Qual segmento atua?" prop="segmentOption">
        <el-select
          v-model="signupForm.segmentOption"
          placeholder="Escolha o segmento"
        >
          <el-option
            v-for="item in segmentOptions"
            :key="item.value"
            :label="item.label"
            :value="item.value"
          >
          </el-option>
        </el-select>
      </el-form-item>
      <el-form-item
        label="Site da empresa"
        prop="website"
        placeholder="www.minhaempresa.com.br"
      >
        <el-input v-model="signupForm.website"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="nextStep()" class="btn-next"
          >Avançar</el-button
        >
      </el-form-item>
    </el-form>
  </div>
</template>

<script lang="ts">
import Vue from 'vue';
export default Vue.extend({
  name: 'AboutCompanyStep',
  data() {
    return {
      rules: {
        name: [
          {
            required: true,
            message: 'Insira o nome da empresa.',
            trigger: 'blur',
          },
        ],
      },

      segmentOptions: [
        {
          value: 'ecommerce',
          label: 'E-commerce',
        },
        {
          value: 'saas',
          label: 'Software como serviço (Saas)',
        },
        {
          value: 'retail',
          label: 'Comercio varejista físico',
        },

        {
          value: 'others',
          label: 'Outros',
        },
      ],
    };
  },
  computed: {
    cnpj: {
      get() {
        return this.$store.state.signup.cnpj;
      },
      set(value: string) {
        this.$store.commit('setCnpj', value);
      },
    },
    // segmentOption: {
    //   set(value: string) {
    //     this.$store.commit('setSegmentOption', value);
    //   },
    // },
    // website: {
    //   set(value: string) {
    //     this.$store.commit('setWebsite', value);
    //   },
    // },
    signupForm: {
      get() {
        return {
          name: this.$store.state.signup.name,
          cnpj: this.$store.state.signup.cnpj,
          website: this.$store.state.signup.website,
          segmentOption: this.$store.state.signup.segmentOption,
        };
      },
      set(value: string) {
        this.$store.commit('setName', { name: value });
        // this.$store.commit('setCnpj', value);
        // this.$store.commit('setWebsite', value);
        // this.$store.commit('setsegmentOption', value);
      },
    },
  },
  methods: {
    nextStep() {
      (this.$refs['signupForm'] as HTMLFormElement).validate(
        (valid: boolean) => {
          if (valid) {
            this.$store.commit('incrementCurrentStep');
          } else {
            console.log('error submit!!');
            return false;
          }
        }
      );
    },
  },
});
</script>
