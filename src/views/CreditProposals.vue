<template>
  <div>
    <el-row class="proposal-cards">
      <ProposalCard :interestRate="5" :offerAmount="1000" :proposalIndex="1" />
    </el-row>
  </div>
</template>

<script lang="ts">
import Vue from 'vue';
import ProposalCard from '@/components/ProposalCard.vue';

export default Vue.extend({
  name: 'CreditProposals',
  components: {
    ProposalCard,
  },
});
</script>

<style scoped>
.proposal-cards {
  display: flex;
  justify-content: center;
  padding-top: 2rem;
}
</style>
