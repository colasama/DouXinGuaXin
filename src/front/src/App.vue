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
          <a-button type="primary" style="margin-left:20px">
            注册
          </a-button>
        </a-menu>
      </a-layout-header>
    </a-layout>
    <router-view style="text-align: center;margin-top:2px"/>
  </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

.components-layout-demo-top-logo {
  width: 83px;
  height: 40px;
  background: url("assets/8340_logo_green.png");
  margin: 16px 24px 16px 0;
  float: left;
}

.re-header{
  background: rgb(255,255,255);
}

.header-menu{
  width: 100%;
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
    toBook(){
      this.current='book';
      this.$router.push({path:"/book"});
    },
    toIndex(){
      this.current='index';
      this.$router.push({path:"/"});
    },
    toMovie(){
      this.current='movie';
      this.$router.push({path:"/movie"});
    },
    toTopic(){
      this.current='topic';
      this.$router.push({path:"/topic"});
    },
    toGroup(){
      this.current='group';
      this.$router.push({path:"/group"});
    }
  }
};
</script>