<template>
  <div>
  <a-layout >
      <a-layout-content class="fugai-layout-content" >
      <a-row type="flex" justify="center">
        <a-col :span="8">
        </a-col>
        <a-col :span="8">
        
        <a-card style="width:300px;text-align: center;margin-top:50px">
          <h2>注册</h2>
          <a-input placeholder="用户名" ref="usernameInput" v-model="username" style="margin-top:20px">
            <a-icon slot="prefix" type="user" />
          </a-input>
          <a-input placeholder="密码" ref="passwordInput" type="password" v-model="password" style="margin-top:20px">
            <a-icon slot="prefix" type="info-circle" />
          </a-input>
          <a-input placeholder="重复密码" ref="repasswordInput" type="password" v-model="repassword" style="margin-top:20px">
            <a-icon slot="prefix" type="info-circle" />
          </a-input>
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
        </a-col>
        <a-col :span="8">
        </a-col>
        </a-row>
      </a-layout-content>
      <a-layout-footer><h6>书籍影视交流平台</h6></a-layout-footer>
    </a-layout>
  </div>
</template>
