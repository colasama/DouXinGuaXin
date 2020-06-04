<template>
  <div>
  <a-layout class="wrapper">
      <a-layout-content class="contenter" >
        <a-card style="width:300px;margin:100px auto;">
          <h2>登录</h2>
          <a-input placeholder="用户名" ref="usernameInput" v-model="username" style="margin-top:20px">
            <a-icon slot="prefix" type="user" />
          </a-input>
          <a-input-password placeholder="密码" ref="passwordInput" v-model="password" style="margin-top:20px">
            <a-icon slot="prefix" type="info-circle" />
          </a-input-password>
          <a-row type="flex" justify="center" style="margin-top:40px;margin-bottom:30px">
          <a-col :span="11" style="margin-right:10px">
          <a-button type="primary" block>注册</a-button>
          </a-col>
          <a-col :span="11">
          <a-button type="primary" block>登录</a-button>
          </a-col>
          </a-row>
        </a-card>
      </a-layout-content>
      <a-layout-footer class="footer"><h6>书籍影视交流平台</h6></a-layout-footer>
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

.footer{
  flex: 0;
  position:absolute;
  bottom:0;
  width:100%;
  background: rgb(227, 232, 236);
}
</style>