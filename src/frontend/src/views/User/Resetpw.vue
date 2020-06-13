<template>
  <div>
  <a-layout style="min-height:100%">
      <a-layout-content>
        <a-card style="width:300px;margin:100px auto;">
          <h2>重设密码</h2>
          <a-input-password placeholder="请输入新的密码" ref="npasswordInput" v-model="npassword" style="margin-top:20px">
            <a-icon slot="prefix" type="info-circle" />
          </a-input-password>
          <a-input-password placeholder="请重复输入新的密码" ref="nnpasswordInput" v-model="nnpassword" style="margin-top:20px">
            <a-icon slot="prefix" type="info-circle" />
          </a-input-password>
          <a-button type="primary" block @click="resetPasswd" style="margin-top:20px">提交</a-button>
        </a-card>
      </a-layout-content>
  </a-layout>
  </div>
</template>

<style>

</style>

<script>
import Vue from 'vue'
import global_ from '../../components/Global'
export default{
    data() {
      return {
          npassword:"",
          nnpassword:"",
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
        toLogin(){
        this.$router.push({path:"/login"});
        },
        toIndex(){
            if(global_.token!=''){
            global_.username=this.username;
            console.log(global_.token+this.username)
            this.$router.push({path:"/"});
            }
        },
        destroyALL(){
            this.$destroyAll();
        },
        showSuccess(){
            this.$success({
                centered: true,
                title: '重设成功',
                content: "已经可以用新密码登录啦！",//<a-result status="success" title=""/>,
                onOK(){
                    this.destroyALL();
                    this.toLogin();
                }
            })
        },
        resetPasswd(){
            Vue.axios.post(
          'http://182.92.57.178:5000/users/modify_password',
          {
            old_password:this.npassword,
            new_password:this.nnpassword
          },
          {
            headers:{
              'token':global_.token
            }
          }
        ).then((res)=>{
          console.log(res)
        }).catch((res)=>{
          console.log(res)
        })
        }
    }
}
</script>