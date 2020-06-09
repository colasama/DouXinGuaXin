<template>
  <div>
  <a-layout style="min-height:100%">
      <a-layout-content>
        <a-card style="width:300px;margin:100px auto;">
          <h2>忘记密码</h2>
          <a-input placeholder="邮箱" ref="emailInput" v-model="email" style="margin-top:18px">
            <a-icon slot="prefix" type="mail" />
          </a-input>
          <a-button type="primary" block @click="resetPasswd" style="margin-top:20px">发送重设邮件</a-button>
        </a-card>
      </a-layout-content>
  </a-layout>
  </div>
</template>

<style>

</style>

<script>
  import global_ from '../components/Global'
  export default{
    data() {
      return {
        token:'',
      };
    },
    created: function(){
      document.title = this.$route.meta.title || this.$route.meta.pathName
    },
    watch:{
      $route(){
        document.title = this.$route.meta.title || this.$route.meta.pathName
      },   
    },
    methods:{
      toRegister(){
      this.$router.push({path:"/register"});
      },
      toIndex(){
        if(global_.token!=''){
          global_.username=this.username;
          console.log(global_.token+this.username)
          this.$router.push({path:"/"});
        }
      },
      resetPasswd(){//发送重设密码激活右键即可

      }
    }
  }
</script>