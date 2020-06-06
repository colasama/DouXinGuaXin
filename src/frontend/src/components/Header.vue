<template>
  <div class="re-header">
        <div @click ="toIndex" class="top-logo" />
        <a-menu mode="horizontal"  v-model="current" :style="{ lineHeight: '64px' }" class="header-menu">
          <a-menu-item key="index" @click = "toIndex">首页</a-menu-item>
          <a-menu-item key="book" @click = "toBook">书籍</a-menu-item>
          <a-menu-item key="movie" @click = "toMovie">影视</a-menu-item>
          <a-menu-item key="group" @click = "toGroup">小组</a-menu-item>
          <a-menu-item key="topic" @click = "toTopic">话题</a-menu-item>
          
            <a-button type="primary" size="small" @click="toRegister" style="margin-left:10px" v-if="showLogin">
              注册
            </a-button>
            <a-button type="primary" size="small" @click="toLogin" style="margin-left:15px;margin-right:48px" v-if="showLogin">
              登录
            </a-button>
            <a-sub-menu key="topic" v-if="showExit">
              <span>
                <a-icon/>欢迎您：{{username_head}}
              </span>
              <a-menu-item-group title="Item 1">
                <a-menu-item key="setting:1">Option 1</a-menu-item>
                <a-menu-item key="setting:2" @click="exit">登出</a-menu-item>
              </a-menu-item-group>
            </a-sub-menu>
        </a-menu>
  </div>
</template>

<style>
.top-logo {
  cursor: pointer;
  width: 83px;
  height: 40px;
  background: url("../assets/8340_logo_green.png");
  margin: 14px 48px 0px 48px;
  float: left;
}

.re-header{
  background: rgb(255,255,255);
  height: 62px;
  text-align:center;
  
}

.header-menu{
  text-align:right;
}
</style>



<script>
import global_ from '../components/Global'
export default {
  data() {
    return {
      showExit:false,
      showLogin:true,
      current: ['index'],
    };
  },
  created: function(){
    document.title = this.$route.meta.title || this.$route.meta.pathName
    console.log(global_.token)
    console.log('head has been created')
  },
  computed:{
    token_head:function(){
      console.log('token has changed');
      console.log("是否已登录");
      console.log(global_.token!='');
      return global_.token;
    },
    username_head:function(){
      return global_.username;
    }
  },
  watch:{
    $route(){
      document.title = this.$route.meta.title || this.$route.meta.pathName
    },
    token_head:function(newval){
      if(newval=='')
        this.showExit=false,this.showLogin=true;
      else
        this.showExit=true,this.showLogin=false;
    }
  },
  methods: {
    exit(){
      this.showExit=false;
      this.showLogin=true;
    },
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