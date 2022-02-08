<template>
  <el-dialog :visible.sync="isDialogVisible" width="30%" class="error-dialog">
    <font-awesome-icon
      :icon="['far', 'times-circle']"
      size="6x"
      class="error-icon"
    />
    <div>
      <h1>Occorreu um erro!</h1>
      <p>{{ message }}</p>
      <span><strong>Status:</strong> {{ status }}</span>
    </div>

    <el-button type="primary" @click="isDialogVisible = false" class="close-btn"
      >Ok</el-button
    >
  </el-dialog>
</template>
<script lang="ts">
import Vue from 'vue';
export default Vue.extend({
  name: 'ErrorDialog',
  props: {
    message: { type: String, required: true },
    status: { type: Number, required: true },
    isDialogVisible: { type: Boolean, required: true },
  },
});
</script>
<style scoped>
.error-icon {
  color: #f56c6c;
  margin-bottom: 1rem;
}
.error-dialog {
  text-align: center;
}
.close-btn {
  margin-top: 1rem;
}
</style>
