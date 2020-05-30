<template>
  <div>
    <a-layout>
      <a-layout-header class="re-header">
        <div class="components-layout-demo-top-logo" />
        
        <a-menu mode="horizontal"  v-model="current" :style="{ lineHeight: '64px' }" class="header-menu">

          <a-menu-item key="index" @click = "toIndex">首页</a-menu-item>
          <a-menu-item key="book" @click = "toBook">书籍</a-menu-item>

          <a-menu-item key="movie" @click = "toMovie">影视</a-menu-item>
          <a-menu-item key="group" @click = "toGroup">小组</a-menu-item>
          <a-menu-item key="topic" @click = "toTopic">话题</a-menu-item>
          <a-button type="primary" size="small" @click="toRegister" style="margin-left:10px">
            注册
          </a-button>
          <a-button type="primary" size="small" @click="toLogin" style="margin-left:15px">
            登录
          </a-button>
        </a-menu>
      </a-layout-header>
    </a-layout>
    <router-view style="text-align: center;margin-top:4px"/>
  </div>
</template>

<style>

.components-layout-demo-top-logo {
  width: 83px;
  height: 40px;
  background: url("assets/8340_logo_green.png");
  margin: 14px 0px 0px 0;
  float: left;
}

.re-header{
  background: rgb(255,255,255);
  height: 62px;
}

.header-menu{
  text-align:right;
}
</style>


<script>
export default {
  data() {
    return {
      current: ['index'],
    };
  },
  methods: {
    toIndex(){
      this.current='index';
      this.$router.push({path:"/"});
    },
    toBook(){
      this.current='book';
      this.$router.push({path:"/book/index"});
    },
    toMovie(){
      this.current='movie';
      this.$router.push({path:"/movie/index"});
    },
    toTopic(){
      this.current='topic';
      this.$router.push({path:"/topic/index"});
    },
    toGroup(){
      this.current='group';
      this.$router.push({path:"/group/index"});
    },
    toRegister(){
      this.current='register';
      this.$router.push({path:"/register"});
    },
    toLogin(){
      this.current='login';
      this.$router.push({path:"/login"});
    }
  }
};
</script>