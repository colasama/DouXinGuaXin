<template>
  <div>
  <a-layout class="wrapper" >
      <a-layout-content class="contenter" >

        <div style="width:300px;margin:100px auto;">
        <a-card>
          <h2>注册</h2>
          <a-input placeholder="用户名" ref="usernameInput" v-model="username" style="margin-top:20px">
            <a-icon slot="prefix" type="user" />
          </a-input>
          <a-input-password placeholder="密码" ref="passwordInput" v-model="password" style="margin-top:20px">
            <a-icon slot="prefix" type="info-circle" />
          </a-input-password>
          <a-input-password placeholder="重复密码" ref="repasswordInput" v-model="repassword" style="margin-top:20px">
            <a-icon slot="prefix" type="info-circle" />
          </a-input-password>
          <a-input placeholder="邮箱" ref="emailInput" v-model="email" style="margin-top:20px">
            <a-icon slot="prefix" type="mail" />
          </a-input>
          <a-input placeholder="手机" ref="phoneInput" v-model="phone" style="margin-top:20px">
            <a-icon slot="prefix" type="phone" />
          </a-input>
          <a-row type="flex" justify="center" style="margin-top:30px;margin-bottom:20px">
          <!--a-col :span="11" style="margin-right:10px">
          <a-button type="primary" block>登录</a-button>
          </a-col-->
          <a-col :span="24">
          <a-button type="primary" block>注册</a-button>
          </a-col>
          </a-row>
        </a-card>
        </div>
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
</style>