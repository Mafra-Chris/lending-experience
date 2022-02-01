<template>
  <div>
    <div>
      <h1 class="login-title">{{ stepsTitle[currentStep] }}</h1>
    </div>
    <el-progress :percentage="progressPerc" class="progress-bar"></el-progress>
    <div v-if="currentStep === 0">
      <AboutCompanyStep />
    </div>
    <div v-else-if="currentStep === 1">
      <RevenueStep />
    </div>
    <div v-else-if="currentStep === 2">
      <RegisterStep />
    </div>
  </div>
</template>

<script lang="ts">
import Vue from 'vue';
import AboutCompanyStep from './AboutCompanyStep.vue';
import RevenueStep from './RevenueStep.vue';
import RegisterStep from './RegisterStep.vue';
export default Vue.extend({
  name: 'Signup',
  components: {
    AboutCompanyStep,
    RevenueStep,
    RegisterStep,
  },
  data() {
    return {
      stepsTitle: [
        'Fale sobre a empresa',
        'Situação financeira',
        'Dados para cadastro',
      ],
    };
  },
  computed: {
    progressPerc: {
      get() {
        return this.$store.state.signup.progressPerc;
      },
    },
    currentStep: {
      get() {
        return this.$store.state.signup.currentStep;
      },
    },
  },
});
</script>
<style>
.el-form .el-select {
  width: 100%;
}
.progress-bar {
  margin-bottom: 1.2rem;
}
</style>
