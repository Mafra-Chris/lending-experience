<template>
  <div>
    <el-form
      :rules="rules"
      ref="signupForm"
      :model="signupForm"
      label-position="top"
    >
      <el-form-item label="Nome" prop="name">
        <el-input v-model="name"></el-input>
      </el-form-item>
      <el-form-item
        label="Para qual CNPJ deseja solicitar crédito?"
        prop="cnpj"
        placeholder="00.000.000/0000-00"
      >
        <el-input v-model="cnpj"></el-input>
      </el-form-item>
      <el-form-item label="Qual segmento atua?" prop="segmentOption">
        <el-select v-model="segmentOption" placeholder="Escolha o segmento">
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
        <el-input v-model="website"></el-input>
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
    const verifySector = (digits: number, cnpj: string) => {
      const slice = cnpj.slice(0, digits);
      let factor = digits - 7;
      let sum = 0;

      for (let i = digits; i >= 1; i--) {
        const n = parseInt(slice[digits - i]);
        sum += n * factor--;
        if (factor < 2) factor = 9;
      }

      const result = 11 - (sum % 11);

      return result > 9 ? 0 : result;
    };

    let validateCNPJ = (rule: object, value: string, callback: Function) => {
      let cnpj = value.replace(/[^\d]+/g, '');
      const items = [...new Set(cnpj)];
      const digits = cnpj.slice(12);

      // Valida 1o. dígito verificador
      const digit0 = verifySector(12, cnpj);
      if (digit0.toString() !== digits[0])
        return callback(new Error('Por favor, verifique se o CNPJ é válido'));

      // Valida 2o. dígito verificador
      const digit1 = verifySector(13, cnpj);
      if (digit1.toString() !== digits[1])
        return callback(new Error('Por favor, verifique se o CNPJ é válido'));

      if (cnpj.length !== 14 || items.length === 1)
        return callback(new Error('Por favor, verifique se o CNPJ é válido'));

      return callback();
    };
    return {
      rules: {
        name: [
          {
            required: true,
            message: 'Insira o nome da empresa.',
            trigger: 'blur',
          },
        ],
        cnpj: [
          {
            required: true,
            message: 'Obrigatório.',
            trigger: 'blur',
          },
          { validator: validateCNPJ, trigger: 'blur' },
        ],
        segmentOption: [
          {
            required: true,
            message: 'Obrigatório.',
            trigger: 'blur',
          },
        ],
        website: [
          {
            required: true,
            message: 'Obrigatório.',
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
    name: {
      get() {
        return this.$store.state.signup.name;
      },
      set(value: string) {
        this.$store.commit('setName', { name: value });
      },
    },
    cnpj: {
      get() {
        return this.$store.state.signup.cnpj;
      },
      set(value: string) {
        let cnpj = value.replace(/[^\d]+/g, '');
        cnpj = cnpj.replace(
          /^(\d{2})(\d{3})(\d{3})(\d{4})(\d{2})/,
          '$1.$2.$3/$4-$5'
        );
        this.$store.commit('setCnpj', { cnpj: cnpj });
      },
    },
    segmentOption: {
      get() {
        return this.$store.state.signup.segmentOption;
      },
      set(value: string) {
        this.$store.commit('setSegmentOption', { segmentOption: value });
      },
    },
    website: {
      get() {
        return this.$store.state.signup.website;
      },
      set(value: string) {
        this.$store.commit('setWebsite', { website: value });
      },
    },
    signupForm(): object {
      return {
        name: this.name,
        cnpj: this.cnpj,
        website: this.website,
        segmentOption: this.segmentOption,
      };
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
