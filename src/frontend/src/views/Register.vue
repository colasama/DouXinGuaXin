<template>
  <div>
  <a-layout style="min-height:100%">
      <a-layout-content>

        <div style="width:300px;margin:100px auto;">
        <a-card>
          <h2>注册</h2>
          <a-input placeholder="用户名" ref="usernameInput" v-model="username" style="margin-top:18px">
            <a-icon slot="prefix" type="user" />
          </a-input>
          <a-input-password placeholder="密码" ref="passwordInput" v-model="password" style="margin-top:18px">
            <a-icon slot="prefix" type="info-circle" />
          </a-input-password>
          <a-input-password placeholder="重复密码" ref="repasswordInput" v-model="repassword" style="margin-top:18px">
            <a-icon slot="prefix" type="info-circle" />
          </a-input-password>
          <a-input placeholder="邮箱" ref="emailInput" v-model="email" style="margin-top:18px">
            <a-icon slot="prefix" type="mail" />
          </a-input>
          <a-input placeholder="手机" ref="phoneInput" v-model="phonenum" style="margin-top:18px">
            <a-icon slot="prefix" type="phone" />
          </a-input>
          <a-row type="flex" justify="start" >
            <a-col :span="20" type="flex" v-if="showerr" style="margin-top:10px">
              <p class="font-control">{{errorTip}}</p>
            </a-col>
          </a-row>
          <a-row type="flex" justify="center" style="margin-top:10px">
            <!--a-col :span="11" style="margin-right:10px">
            <a-button type="primary" block>登录</a-button>
            </a-col-->
            <a-col :span="24">
              <a-button type="primary" block @click="register">注册</a-button>
            </a-col>
          </a-row>
        </a-card>
        </div>

        <a-modal 
                centered="true"
                title="注册成功"
                :visible="successVisible"
                :confirm-loading="confirmLoading"
                @ok="handleOk"
                @cancel="handleCancel"
                okText="确认"
                cancelText="等一下再过去"
                >
                <a-result
                  status="success"
                  title="欢迎来到豆辛瓜辛!"
                  sub-title="点击确认键来登录吧！"
                >
                </a-result>
            </a-modal>
      </a-layout-content>
    </a-layout>
  </div>
</template>

<style>
.wrapper{
  display:flex;
  flex-direction:column;
  min-height:100%;
}

.contenter{
    text-align: center;
    position:absolute;
    width:100%;
    height: calc(100% - 100px) ;
    background: rgb(240, 242, 245);
  }

.font-control{
  color:crimson;
  font-size: 15px;
  text-align: left;
}
</style>

<script>
  import Vue from 'vue'
  export default{
  data() {
      return {
        showerr:false,
        errorTip:'',
        username:'',
        password:"",
        repassword:"",
        email:'',
        phonenum:'',
        message:[],
        successVisible:false,
        
      };
    },
    methods:{ 
      toLogin(){
        console.log("toLogin Function")
        this.$router.push({path:"/login"});
    },
      destroyALL(){
        this.$destroyAll();
      },
      handleOk(){
        this.successVisible=false;
        this.$router.push({path:"/login"});
      },
      handleCancel(){
        this.successVisible=false;
      },
      showSuccess(){
        this.successVisible=true;
        /*var se = this;
        this.$success({
          centered: true,
          title: '注册成功',
          content: "按下ok键跳转到登录页面！",//<a-result status="success" title=""/>,
          onOK(){
            console.log("toLogin Function");
            se.$router.push({path:"/login"});
            }
        })*/
      },
      register(){
        var regEmail = /^[A-Za-z0-9\u4e00-\u9fa5]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$/;
        var regPhone = /^[0-9]{11}$/;
        this.errorTip='';
        if(this.username=='')
          this.errorTip='请输入您的用户名';
        else if(this.password==""||this.repassword=="")
          this.errorTip='请输入您的密码';
        else if(this.email=='')
          this.errorTip='请输入您的邮箱';
        else if(this.phonenum=='')
          this.errorTip='请输入您的手机号码';
        else if(!regEmail.test(this.email))
          this.errorTip='请输入正确的邮箱';
        else if(!regPhone.test(this.phonenum))
          this.errorTip='请输入正确的手机号码';
        else if(this.password!=this.repassword)
          this.errorTip='两次输入的密码不同';
        if(this.errorTip!=''){
          this.showerr=true;
          return;
        }
        else 
          this.showerr=false;
        Vue.axios.post('http://182.92.57.178:5000/register',{
            name:this.username,
            password:this.password,
            email:this.email,
            phonenum:this.phonenum
        }).then(function(res){
          console.log(res.data);
          this.showSuccess();
        }).catch(function(error){
          console.log(error); 
        })
        
      }
    }
  }
</script>