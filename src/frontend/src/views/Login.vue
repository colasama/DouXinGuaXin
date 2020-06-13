<template>
  <div>
  <a-layout style="min-height:100%">
      <a-layout-content>
        <a-card style="width:300px;margin:100px auto;">
          <h2>登录</h2>
          <a-input placeholder="用户名" ref="usernameInput" v-model="username" style="margin-top:20px">
            <a-icon slot="prefix" type="user" />
          </a-input>
          <a-input-password placeholder="密码" ref="passwordInput" v-model="password" style="margin-top:20px">
            <a-icon slot="prefix" type="info-circle" />
          </a-input-password>
          <a-button type="link" @click="toResetpw" style="text-align:right;margin:10px 0 0 0;">忘记密码？</a-button>
          <div v-if="errorLogin" style="color:red">用户名或密码错误！</div>
          <a-row type="flex" justify="center" style="margin-top:10px;margin-bottom:30px">
          <a-col :span="11" style="margin-right:10px">
          <a-button type="primary" block @click="toRegister">注册</a-button>
          </a-col>
          <a-col :span="11">
          <a-button type="primary" block @click="checklogin">登录</a-button>
          </a-col>
          </a-row>
        </a-card>
      </a-layout-content>
  </a-layout>
  </div>
</template>

<style>

</style>

<script>
  import Vue from 'vue'
  import global_ from '../components/Global'
  import Bus from '../bus.js'
  export default{
    data() {
      return {
        username:'',
        password:"",
        token:'',
        count:"",
        errorLogin: false,
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
      toResetpw(){
        this.$router.push({path:"/forgetpw"});
      },
      toRegister(){
      this.$router.push({path:"/register"});
      },
      changeCurrent(){
        Bus.$emit('current','index')
      },
      toIndex(){
        this.$router.push({path:"/"});
      },
      checklogin(){
        var self = this;
        Vue.axios.post('http://182.92.57.178:5000/login',{
            name:this.username,
            password:this.password
        }).then(function(res){
          global_.username=self.username;
          console.log(global_.username);
          global_.token=res.data.result.token;
          //console.log("Login Page: "+global_.token);
          self.startDivi();
          //self.$router.push({path:"/"});
          //self.destroyALL();
          Vue.axios.get('http://182.92.57.178:5000/users/groups',{headers:{"token":global_.token}}).then(function(res){
            global_.my_groups=res.data.result;
          }).catch(function(error){
            console.log(error,Response);
          })
          Vue.axios.get('http://182.92.57.178:5000/users/topics',{headers:{"token":global_.token}}).then(function(res){
            global_.my_topics=res.data.result;
          }).catch(function(error){
            console.log(error);
          })
          Vue.axios.get('http://182.92.57.178:5000/users/book_comments',{headers:{"token":global_.token}}).then(function(res){
            global_.my_book_comments=res.data.result;
          }).catch(function(error){
            console.log(error);
          })
          Vue.axios.get('http://182.92.57.178:5000/users/movie_comments',{headers:{"token":global_.token}}).then(function(res){
            global_.my_movie_comments=res.data.result;
          }).catch(function(error){
            console.log(error);
          })
          Vue.axios.get('http://182.92.57.178:5000/users/reports',{headers:{"token":global_.token}}).then(function(res){
            global_.my_movie_reports=res.data.result.movies;
            global_.my_book_reports=res.data.result.books;
          }).catch(function(error){
            console.log(error);
          })
        }).catch(function(error){
          console.log("nmdwsm");
          console.log(error);

          self.changeErrorLogin();
        })
      },
      changeErrorLogin(){
        this.errorLogin=true;
      },
      startDivi(){
        const TIME_COUNT = 2;
        const hide = this.$message.loading('登陆成功！即将返回首页！', 0);
        setTimeout(hide, 2500);
        if(!this.timer){
            this.count = TIME_COUNT;
            this.show = false;
            this.timer = setInterval(()=>{
            if(this.count > 0 && this.count <= TIME_COUNT){
                this.count--;
            }else{
                this.show = true;
                clearInterval(this.timer);
                this.timer = null;
                //跳转的页面写在此处
                this.changeCurrent();
                this.$router.push({
                    path: '/'
                });
                
            }
          },1000)
        }
        
    },
    }
  }
</script>