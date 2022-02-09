<template>
  <el-menu
    :default-active="'1'"
    class="navbar"
    mode="horizontal"
    background-color="#212842"
    text-color="#fff"
    active-text-color="#77baff"
  >
    <el-menu-item
      ><img src="@/assets/logo.png" alt="" class="logo"
    /></el-menu-item>

    <el-menu-item index="1">Home</el-menu-item>
    <el-menu-item index="2" class="btn-logout"
      ><font-awesome-icon
        icon="sign-out-alt"
        size="lg"
        class="logout-icon"
      ></font-awesome-icon>
      Log Out</el-menu-item
    >
  </el-menu>
</template>

<script lang="ts">
export default {
  name: 'Navbar',
};
</script>

<style scoped>
.btn-logout {
  right: 0;
}

.logout-icon {
  margin-right: 0.25rem;
}

.navbar {
  display: flex;
}
ul > :last-child {
  margin-left: auto;
}
</style>
