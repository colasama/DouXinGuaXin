<template>
  <a-layout id="components-layout-demo-custom-trigger" style="min-height:100%">
    <a-layout-sider v-model="collapsed" :trigger="null" collapsible>
      <div class="logo" />
      <a-menu theme="dark" mode="inline" :default-selected-keys="['1']">
        <a-menu-item key="1">
          <a-icon type="user" />
          <span>用户控制</span>
        </a-menu-item>
        <a-menu-item key="2">
          <a-icon type="control" />
          <span>内容管理</span>
        </a-menu-item>
        <a-menu-item key="3">
          <a-icon type="setting" />
          <span>设置</span>
        </a-menu-item>
      </a-menu>
    </a-layout-sider>
    <a-layout>
      <a-layout-header style="background: #fff; padding: 0">
        
        <a-page-header
            style="border: 1px solid rgb(235, 237, 240)"
            title="控制台"
            sub-title="是管理员管理界面"
        />
      </a-layout-header>
      <a-layout-content
        :style="{ margin: '24px 16px', padding: '24px', background: '#fff', minHeight: '280px' }"
      >
        Content
      </a-layout-content>
    </a-layout>
    
  </a-layout>
  
</template>
<script>
export default {
  data() {
    return {
    };
  },
};
</script>
<style>
#components-layout-demo-custom-trigger .trigger {
  font-size: 18px;
  line-height: 64px;
  padding: 0 24px;
  cursor: pointer;
  transition: color 0.3s;
}

#components-layout-demo-custom-trigger .trigger:hover {
  color: #1890ff;
}

#components-layout-demo-custom-trigger .logo {
  height: 32px;
  margin: 16px;
}
</style>