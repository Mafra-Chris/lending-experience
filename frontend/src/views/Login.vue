<template>
  <div class="home">
    <el-row>
      <el-col :sm="12" class="banner hidden-xs-only"
        ><img src="@/assets/login.jpg" alt="" />
      </el-col>
      <el-col :xs="24" :sm="12" class="login-col">
        <div class="login-container">
          <Login />
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script lang="ts">
import Vue from 'vue';
import 'element-ui/lib/theme-chalk/display.css';
import Login from '../components/Login.vue';
export default Vue.extend({
  name: 'LoginView',
  components: {
    Login,
  },
});
</script>

<style scoped>
.home {
  min-height: 100%;
  text-align: left;
}
.banner {
  height: 100vh;
}

.login-col {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

.login-container {
  width: 85%;
}

@media (min-width: 1024px) {
  .login-container {
    width: 65%;
  }
}
img {
  object-fit: cover;
  width: 100%;
  height: 100%;
}
</style>
