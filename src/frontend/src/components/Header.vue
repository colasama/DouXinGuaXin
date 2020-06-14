<template>
  <div class="re-header">
        <div @click ="toIndex" class="top-logo" />
        
        <a-menu mode="horizontal"  v-model="current" :style="{ lineHeight: '64px' }" class="header-menu">
          <cSearch class="search"/>
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
            <a-dropdown v-if="!showLogin">
              <a-menu slot="overlay">
                <a-menu-item key="1" @click="toUserindex">
                  个人主页
                </a-menu-item>
                <a-menu-item key="3" @click="exit">
                  退出
                </a-menu-item>
              </a-menu> 
              <a-button type="link" @click="toUserindex"> 欢迎回来，{{username}}。 <a-icon type="down" /> </a-button>
            </a-dropdown>
            <!--a-sub-menu key="topic" v-if="showExit">
              <span>
                <a-icon/>欢迎您：{{username_head}}
              </span>
              <a-menu-item-group title="Item 1">
                <a-menu-item key="setting:1">Option 1</a-menu-item>
                <a-menu-item key="setting:2" @click="exit">登出</a-menu-item>
              </a-menu-item-group>
            </a-sub-menu-->
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

.search{
  cursor: pointer;
  height: 40px;
  margin: 0px 0px 0px calc(50vw - 300px);
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
import global_ from '../components/Global';
import cSearch from '../components/Search.vue';
import Bus from '../bus.js'
export default {
  components:{
    cSearch
  },
  data() {
    return {
      showLogin:true,//控制注册登录按钮和按钮菜单的出现
      current: ['index'],
      username:"",
      token:''
    };
  },
  created: function(){
    document.title = this.$route.meta.title || this.$route.meta.pathName
    console.log(global_.token);
    console.log('head has been created');
    this.username=global_.username;
    this.token=global_.token;

    Bus.$on('current',target=>{
      console.log(target);
      this.current=target;
    })
  },
  computed:{
    token_head:function(){
      console.log(global_.token!='');
      return this.global_.token;
    },
    username_head:function(){
      return global_.username;
    }
  },
  watch:{
    $route(){
      document.title = this.$route.meta.title || this.$route.meta.pathName
    },
    current:function(){
      this.username=global_.username;
      this.token=global_.token;
      console.log(this.current);
      console.log(this.username);
    },
    token:function(newval){
      console.log('环境改变');
      if(newval=='')
        this.showLogin=true;
      else
        this.showLogin=false;
    },
    token_head:function(newval){
      if(newval=='')
        this.showLogin=true;
      else
        this.showLogin=false;
    }
  },
  methods: {
    handleMenuClick(){
      this.toUserindex();
    },
    exit(){
      this.showLogin=true;
      global_.token='';
      global_.username='not login';
      global_.loginStatus=false;
      this.toIndex();

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
    },
    toUserindex(){
      this.current='login';
      this.$router.push({
        path:"/user/index",
        query:{
          token:global_.token
        }});
    },
    toUserChange(){
      this.current='login';
    }
  }
};
</script>