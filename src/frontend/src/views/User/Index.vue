<template>
  <div>
  <a-layout style="min-height:100%">
      <a-layout-content>
        <a-page-header
            style="margin-left:28px;margin-top:30px"
            title="个人主页"
            sub-title="Profile"
        />

        <div>
        <a-card
          style="width:90%;margin:24px auto;"
          :tab-list="tabListNoTitle"
          :active-tab-key="noTitleKey"
          @tabChange="key => onTabChange(key, 'noTitleKey')"
        >
          <div v-if="noTitleKey === 'article'" style="margin-bottom:20px">
            <a-avatar :size="128" style="margin-top:20px;color:#f56a00;backgroundColor:#fde3cf" icon="user"></a-avatar>
            <div style="font-size:24px;color:grey;margin:10px" ><b>{{User_name}}</b></div>
            <div style="margin-top:5px">账号：{{User_name}}</div>
            <div style="margin-top:5px">ID: {{id}}</div>
            <div style="margin-top:5px">手机号：{{phonenum}}</div>
            <div style="margin-top:5px">邮箱：{{email}}</div>
            <div style="margin-top:5px" v-if="priv">权限：<a-tag color="orange">小组管理员</a-tag></div>
          </div>
          <div v-else-if="noTitleKey === 'project'">
            <div><a-input placeholder="手机号" style="width:400px;margin-top:20px" v-model="newphone"></a-input></div>
            <div><a-input placeholder="修改邮箱" style="width:400px;margin-top:20px" v-model="newemail"></a-input></div>
            <div><a-input placeholder="昵称" style="width:400px;margin-top:20px" v-model="newname"></a-input></div>
            <div><a-button type="primary" style="width:400px;margin:20px 0 20px 0" @click="resetInfo">保存</a-button></div>
          </div>
        </a-card>
      </div>
      </a-layout-content>
    </a-layout>
  </div>
</template>

<style>
</style>

<script>
import Vue from 'vue'
import global_ from '../../components/Global'
export default {
  data() {
    return {
      token:"null",
      User_name:"",
      id:-1,
      phonenum:"",
      email:"",
      newname:'',
      newphone:"",
      newemail:"",
      priv:"",
      showPriv:false,
      tabList: [
        {
          key: 'tab1',
          // tab: 'tab1',
          scopedSlots: { tab: 'customRender' },
        },
        {
          key: 'tab2',
          tab: 'tab2',
        },
      ],
      contentList: {
        tab1: 'content1',
        tab2: 'content2',
      },
      tabListNoTitle: [
        {
          key: 'article',
          tab: '个人信息',
        },
      ],
      key: 'tab1',
      noTitleKey: 'article',
    };
  },
  created:function(){
    this.getUserInfo();
    console.log(this.token)
  },
  mounted:{
  },
  methods: {
    onTabChange(key, type) {
      console.log(key, type);
      this[type] = key;
    },
    getUserInfo(){
        Vue.axios.get(
          'http://182.92.57.178:5000/users/info',
          {
            headers:{
              'Authorization':global_.token,
              'token':global_.token
            }
          }
        ).then((response)=>{
          console.log(response);
          console.log(response.data.result.User_id);
          this.User_name=response.data.result.User_name;
          this.id=response.data.result.User_id;
          this.phonenum=response.data.result.User_phonenum;
          this.email=response.data.result.User_email;
          this.priv=response.data.result.User_authority;
          if(this.priv!=0)
            this.showPriv=true;
        }).catch(function(response){
          console.log(response);
        })
      },
    resetInfo(){
    }
  },
};
</script>